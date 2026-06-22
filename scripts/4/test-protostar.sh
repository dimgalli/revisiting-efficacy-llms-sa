#!/bin/bash

for challenge in stack0 stack1 stack2 stack3 stack4 stack5 stack6 stack7 format0 format1 format2 format3 format4 heap0 heap1 heap2 heap3 net0 net1 net2 final0 final1 final2
do
    for model in gpt-4.1
    do
        for seed in {0..4}
        do
            docker exec -e OPENAI_API_KEY=REDACTED -it -u user nerve python -m nerve run challenges/protostar/${challenge}.yml -g openai/${model} --max-steps 20 --max-cost 10.0 --timeout 300 2>&1 | tee logs/protostar/protostar-${challenge}-${model}-${seed}.txt
            sleep 10
        done
    done
    for model in llama3.1:8b
    do
        for seed in {0..4}
        do
            docker exec -it -u user nerve python -m nerve run challenges/protostar/${challenge}.yml -g "ollama/${model}?api_base=http://host.docker.internal:11434" --max-steps 20 --max-cost 10.0 --timeout 300 2>&1 | tee logs/protostar/protostar-${challenge}-${model}-${seed}.txt
            sleep 30
        done
    done
done
