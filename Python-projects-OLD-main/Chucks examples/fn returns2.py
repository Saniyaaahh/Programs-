def greet(lang):
    if lang == "es":
        return "Hola"
    elif lang == "fr":
        return "Bonjour"
    else:
        return "Hello"

print(greet("es"), "Miran")
print(greet("fr"), "warner")
print(greet("eng"), "marcus")