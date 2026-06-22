#!/bin/sh

for challenge in level00 level01 level02 level03 level04 level05 level06 level07 level08 level09 level10 level11 level12 level13 level14 level15 level16 level17 level18 level19
do
    for model in gpt-3.5-turbo gpt-4-turbo gpt-4o-mini gpt-4o gpt-4.1-mini gpt-4.1
    do
        docker exec --env-file .env -it -u user testllm-nerve-1 nerve run challenges/nebula/${challenge}.yml -g openai/${model} --max-steps 10 --max-cost 10.0 --timeout 300 2>&1 | tee logs/nebula/nebula-${challenge}-${model}.txt
    done

    #for model in claude-3-5-haiku claude-3-7-sonnet
    #do
    #    docker exec --env-file .env -it -u user testllm-nerve-1 nerve run challenges/nebula/${challenge}.yml -g anthropic/${model} --max-steps 10 --max-cost 10.0 --timeout 300 2>&1 | tee logs/nebula/nebula-${challenge}-${model}.txt
    #done

    #for model in gemini-2.0-flash-lite gemini-2.5-flash gemini-2.5-pro
    #do
    #    docker exec --env-file .env -it -u user testllm-nerve-1 nerve run challenges/nebula/${challenge}.yml -g gemini/${model} --max-steps 10 --max-cost 10.0 --timeout 300 2>&1 | tee logs/nebula/nebula-${challenge}-${model}.txt
    #done

    for model in llama3.1:8b llama3.1:70b llama3.3:70b llama4:16x17b
    do
        docker exec -it -u user testllm-nerve-1 nerve run challenges/nebula/${challenge}.yml -g ollama/${model}?api_base=http://host.docker.internal:11434 --max-steps 10 --max-cost 10.0 --timeout 300 2>&1 | tee logs/nebula/nebula-${challenge}-${model}.txt
    done

    for model in mistral:7b mixtral:8x22b
    do
        docker exec -it -u user testllm-nerve-1 nerve run challenges/nebula/${challenge}.yml -g ollama/${model}?api_base=http://host.docker.internal:11434 --max-steps 10 --max-cost 10.0 --timeout 300 2>&1 | tee logs/nebula/nebula-${challenge}-${model}.txt
    done

    for model in qwen2.5:7b qwen2.5:72b qwen2.5-coder:7b qwen2.5-coder:32b qwen3:8b qwen3:32b qwq:32b
    do
        docker exec -it -u user testllm-nerve-1 nerve run challenges/nebula/${challenge}.yml -g ollama/${model}?api_base=http://host.docker.internal:11434 --max-steps 10 --max-cost 10.0 --timeout 300 2>&1 | tee logs/nebula/nebula-${challenge}-${model}.txt
    done
done