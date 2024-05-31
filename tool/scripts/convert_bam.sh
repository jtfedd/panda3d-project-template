#!/bin/zsh

for file in $1/**/*(.); do
    if [[ $file == *.glb ]]; then
        echo $file
        gltf2bam $file
    fi
done
