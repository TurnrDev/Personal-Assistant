from distutils.util import strtobool
from papy import actions
from papy.utils import ai_say, ai_ask, config, DEFAULT_AI_NAME

def main() -> None:
    # Load names from config
    ai_name = config.get('ai_name', DEFAULT_AI_NAME)
    username = config.get('username')
    
    if username is None:
        username = config.set('username', ai_ask("What would you like me to call you?"))
    
    ai_say(f"Hello {username}, I am {ai_name}. Pleased to meet you.")
    
    # If the AI name has not been set, ask the user if they want the default or not
    if config.get('ai_name') is None:
        happy_with_papi = strtobool(ai_ask(f"Are you happy with my name '{ai_name}'? (y/n)"))
        if happy_with_papi:
            ai_name = config.set('ai_name', DEFAULT_AI_NAME)
        else:
            ai_name = config.set('ai_name', ai_ask("What would you like to call me?"))
    
    while True:
        command = ai_ask(f"How can I help you, {username}?")
        try:
            fun = getattr(actions, command)
        except AttributeError:
            ai_say("I'm not sure about that yet.")
        else:
            fun()

main()
