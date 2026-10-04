import laya


def main():
    agent = laya.load("convaiinnovations/laya")

    state = {
        "task": "The user asks about something they previously told the agent."
    }

    questions = {
        "memory": {
            "type": "noul",
            "instructions": "Should the agent retrieve long-term memory to answer this task?"
        }
    }

    result = agent.predict(state, questions)

    print("Laya result:")
    print(result)


if __name__ == "__main__":
    main()