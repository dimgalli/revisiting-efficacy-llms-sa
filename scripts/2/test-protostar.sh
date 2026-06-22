#!/bin/sh

for challenge in stack0 stack1 stack2 stack3 stack4 stack5 stack6 stack7 format0 format1 format2 format3 format4 heap0 heap1 heap2 heap3 net0 net1 net2 final0 final1 final2
do
    for model in gpt-3.5-turbo gpt-4-turbo gpt-4o-mini gpt-4o gpt-4.1-mini gpt-4.1
    do
        docker exec --env-file .env -it -u user testllm-nerve-1 nerve run challenges/protostar/${challenge}.yml -g openai/${model} --max-steps 20 --max-cost 10.0 --timeout 300 2>&1 | tee logs/protostar/protostar-${challenge}-${model}.txt
    done

    #for model in claude-3-5-haiku claude-3-7-sonnet
    #do
    #    docker exec --env-file .env -it -u user testllm-nerve-1 nerve run challenges/protostar/${challenge}.yml -g anthropic/${model} --max-steps 20 --max-cost 10.0 --timeout 300 2>&1 | tee logs/protostar/protostar-${challenge}-${model}.txt
    #done

    #for model in gemini-2.0-flash-lite gemini-2.5-flash gemini-2.5-pro
    #do
    #    docker exec --env-file .env -it -u user testllm-nerve-1 nerve run challenges/protostar/${challenge}.yml -g gemini/${model} --max-steps 20 --max-cost 10.0 --timeout 300 2>&1 | tee logs/protostar/protostar-${challenge}-${model}.txt
    #done

    for model in llama3.1:8b llama3.1:70b llama3.3:70b llama4:16x17b
    do
        docker exec -it -u user testllm-nerve-1 nerve run challenges/protostar/${challenge}.yml -g ollama/${model}?api_base=http://host.docker.internal:11434 --max-steps 20 --max-cost 10.0 --timeout 300 2>&1 | tee logs/protostar/protostar-${challenge}-${model}.txt
    done

    for model in mistral:7b mixtral:8x22b
    do
        docker exec -it -u user testllm-nerve-1 nerve run challenges/protostar/${challenge}.yml -g ollama/${model}?api_base=http://host.docker.internal:11434 --max-steps 20 --max-cost 10.0 --timeout 300 2>&1 | tee logs/protostar/protostar-${challenge}-${model}.txt
    done

    for model in qwen2.5:7b qwen2.5:72b qwen2.5-coder:7b qwen2.5-coder:32b qwen3:8b qwen3:32b qwq:32b
    do
        docker exec -it -u user testllm-nerve-1 nerve run challenges/protostar/${challenge}.yml -g ollama/${model}?api_base=http://host.docker.internal:11434 --max-steps 20 --max-cost 10.0 --timeout 300 2>&1 | tee logs/protostar/protostar-${challenge}-${model}.txt
    done
done