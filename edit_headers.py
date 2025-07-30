import argparse
import os

def edit_headers(target_language = "en"):
    translation_dict = {
        "Sample Preparation":{
            "en":"Sample Preparation",
            "es":"Preparación de la muestra",
            "pt":"Preparação da amostra",
            "cs":"Příprava vzorku",
        },
        "Sample Acquisition":{
            "en":"Sample Acquisition",
            "es":"Adquisición de muestras",
            "pt":"Aquisição da amostra",
            "cs":"Snímání vzorku",
        },
        "Image Analysis and Data Handling":{
            "en":"Image Analysis and Data Handling",
            "es":"Análisis de Imágenes y Manejo de Datos",
            "pt":"Análise de imagens e tratamento de dados",
            "cs":"Analýza obrazu a práce s daty",
        },
        "Data Interpretation":{
            "en":"Data Interpretation",
            "es":"Interpretación de Datos",
            "pt":"Interpretação de dados",
            "cs":"Interpretace dat",
        },
        "Additional Resources":{
            "en":"Additional Resources",
            "es":"Recursos Adicionales",
            "pt":"Recursos Adicionais",
            "cs":"Další zdroje",
        },
    }

    lines = open("_toc.yml", "r").readlines()
    newlines = []
    for line in lines:
        for caption in translation_dict.keys():
            if line == f"- caption: {caption}\n":
                line=line.replace(caption,translation_dict[caption][target_language])
        newlines.append(line)
    
    with open("_toc.yml","w") as toc:
        toc.writelines(newlines)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Say what language to translate the headers to")

    parser.add_argument("target_language", help="Language to translate header language into. Currently supported options are en, es, pt, and cs")

    args = parser.parse_args()

    edit_headers(target_language=args.target_language)
