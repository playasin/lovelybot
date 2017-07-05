from microsoftbotframework import ReplyToActivity

def echo_response(message):
  if message["type"] == "message":
"""
    data = {
      "documents": [
        {
          "language": "en",
          "id": "1",
          "text": message["text"]
        }
      ]
    }
    
    headers = {
      'Ocp-Apim-Subscription-Key': 'd1f12664609d42f8a4929eb18b69fc40',
      'Content-Type': 'application/json',
      'Accept': 'application/json',
    }
    
    r = requests.post(
      "https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment",
      data=json.dumps(data),
      headers=headers
    )
    
    emo_score = r.json()["documents"][0]["score"]
    msg = "emotion score is %s\n" % emo_score

    if emo_score > 0.5:
      msg = msg + "You look happy!"
    else:
      msg = msg + "You look unhappy.."

    print(msg)
"""
    ReplyToActivity(fill = message,
                    text = message["text"]).send()
