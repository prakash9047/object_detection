def prettier(results):
    if not isinstance(results, list):
        print("Error: Results must be a list.")
        return

    for item in results:
        if not isinstance(item, dict):
            print("Error: Each item in results must be a dictionary.")
            continue
        
        if 'score' not in item or 'label' not in item or 'box' not in item:
            print("Error: Each item in results must contain 'score', 'label', and 'box' keys.")
            continue
        
        score = round(item.get('score', 0), 3)
        label = item.get('label', 'Unknown')
        box = item.get('box', {})
        if not isinstance(box, dict):
            print("Error: 'box' must be a dictionary.")
            continue

        location = [round(value, 2) for value in box.values()]
        print(f"Detected {label} with confidence {score} at location {location}")
