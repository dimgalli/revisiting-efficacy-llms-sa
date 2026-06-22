#!/bin/bash

for challenge in ret2win split callme write4 badchars fluff pivot ret2csu
do
    for model in gpt-4.1
    do
        for seed in {0..4}
        do
            docker exec -e OPENAI_API_KEY=REDACTED -it -u user nerve python -m nerve run challenges/ropemporium/${challenge}.yml -g openai/${model} --max-steps 20 --max-cost 10.0 --timeout 300 2>&1 | tee logs/ropemporium/ropemporium-${challenge}-${model}-${seed}.txt
            sleep 10
        done
    done
    for model in llama3.1:8b
    do
        for seed in {0..4}
        do
            docker exec -it -u user nerve python -m nerve run challenges/ropemporium/${challenge}.yml -g "ollama/${model}?api_base=http://host.docker.internal:11434" --max-steps 20 --max-cost 10.0 --timeout 300 2>&1 | tee logs/ropemporium/ropemporium-${challenge}-${model}-${seed}.txt
            sleep 30
        done
    done
done
