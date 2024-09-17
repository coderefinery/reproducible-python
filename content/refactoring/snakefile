# the comma is there because glob_wildcards returns a named tuple
numbers, = glob_wildcards("input-images/stars-{number}.png")


# rule that collects the target files
rule all:
    input:
        expand("results/{number}.txt", number=numbers)


rule process_data:
    input:
        "input-images/stars-{number}.png"
    output:
        "results/{number}.txt"
    log:
        "logs/{number}.txt"
    shell:
        """
        python countstars.py --image-file {input} --output-file {output}
        """
