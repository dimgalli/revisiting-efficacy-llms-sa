#!/bin/bash

for challenge in level00 level01 level02 level03 level04 level05 level06 level07 level08 level09 level10 level11 level12 level13 level14 level15 level16 level17 level18 level19
do
    for model in gpt-4.1
    do
	for seed in {0..4}
	do
            docker exec -e OPENAI_API_KEY=REDACTED -it -u user nerve python -m nerve run challenges/nebula/${challenge}.yml -g openai/${model} --max-steps 10 --max-cost 10.0 --timeout 300 2>&1 | tee logs/nebula/nebula-${challenge}-${model}-${seed}.txt

            sleep 10
        done
    done
    for model in llama3.1:8b
    do
	for seed in {0..4}
	do
            docker exec -it -u user nerve python -m nerve run challenges/nebula/${challenge}.yml -g "ollama/${model}?api_base=http://host.docker.internal:11434" --max-steps 10 --max-cost 10.0 --timeout 300 2>&1 | tee logs/nebula/nebula-${challenge}-${model}-${seed}.txt
            sleep 30
        done
    done
done
