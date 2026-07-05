import json

with open('/Users/melanieabalde/.gemini/antigravity-ide/brain/faa6e059-958c-490f-b0a5-93f4c90b912a/.system_generated/logs/transcript_full.jsonl') as f:
    for i, line in enumerate(f):
        if i == 288:
            data = json.loads(line)
            tc = data['tool_calls'][0]
            content = tc['args']['ReplacementContent']
            
            content = content.replace('\\n', '\n')
            content = content.replace('\\"', '"')
            content = content.replace('\\\\', '\\')
            
            with open('src/bento_markup_288.txt', 'w') as out:
                out.write(content)
            print("Successfully extracted log line 288!")
