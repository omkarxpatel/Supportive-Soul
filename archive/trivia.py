
##################
#     TRIVIA     #
##################


async def start_trivia_game(channel):
    question_prompt = "What is a trivia question about mental health or health in general?"
    question = generate_chatgpt_response(question_prompt)

    options_prompt = "What are some answer options for the following question: " + question + "?"
    options = generate_chatgpt_response(options_prompt)

    await channel.send(question)
    await channel.send(f'Options:\n{options}')

    def check_answer(m):
        return m.author != bot.user and m.channel == channel

    # Wait for the user's answer
    try:
        user_response = await bot.wait_for('message', check=check_answer, timeout=30.0)
    except asyncio.TimeoutError:
        await channel.send('Time is up! The correct answer was: ' + get_correct_answer(question))
    else:
        if user_response.content.lower() == get_correct_answer(question).lower():
            await channel.send('Correct answer!')
        else:
            await channel.send('Wrong answer! The correct answer was: ' + get_correct_answer(question))

def generate_chatgpt_response(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

def get_correct_answer(question):
    return 'Option A'