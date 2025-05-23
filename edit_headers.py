import argparse
import os

def edit_headers(target_language = "en"):
    translation_dict = {
        "Sample Preparation":{
            "en":"Sample Preparation",
            "es":"Sample Preparation",
            "pt":"Sample Preparation",
            "cs":"Sample Preparation",
        },
        "Sample Acquisition":{
            "en":"Sample Acquisition",
            "es":"Sample Acquisition",
            "pt":"Sample Acquisition",
            "cs":"Sample Acquisition",
        },
        "Image Analysis and Data Handling":{
            "en":"Image Analysis and Data Handling",
            "es":"Image Analysis and Data Handling",
            "pt":"Image Analysis and Data Handling",
            "cs":"Image Analysis and Data Handling",
        },
        "Data Interpretation":{
            "en":"Data Interpretation",
            "es":"Data Interpretation",
            "pt":"Data Interpretation",
            "cs":"Data Interpretation",
        },
        "Additional Resources":{
            "en":"Additional Resources",
            "es":"Additional Resources",
            "pt":"Additional Resources",
            "cs":"Additional Resources",
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