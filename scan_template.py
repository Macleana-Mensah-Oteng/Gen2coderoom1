import json
import os

def main():
    template_path = os.environ.get("TEMPLATE_PATH", "template.yaml")

    if not os.path.exists(template_path):
        results = {
            "status": "error",
            "message": f"CloudFormation template not found at {template_path}"
        }
    else:
        # Dummy scan logic
        results = {
            "status": "success",
            "message": f"CloudFormation template '{template_path}' scanned successfully."
        }

    with open("results.json", "w") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    main()
