from tts import read_text


text = "Le terme DevOps est utilisé pour décrire l'ensemble des pratiques, processus et équipes qui collaborent ensemble pour créer des applications informatiques."
# text = "The term DevOps is used to describe the set of practices, processes, and teams that work together to create IT applications."
# text = """
# Le terme DevOps est utilisé pour décrire l'ensemble des pratiques, processus et équipes qui collaborent ensemble pour créer des applications informatiques. Cela comprend les processus de développement, la gestion des opérations
# et les équipes de support. Le but est d'assurer une collaboration efficace entre les équipes de développement et d'opérations pour créer des applications de qualité, qui sont fiable et scalable. Les DevOps ont été créés pour résoudre
# """

# text = text.strip()
# text = text.replace("\n", "")
# text = text.replace("\"", "'")

print("TTS")
# read_text('hello')
# read_text('bonjour')
read_text(text)
