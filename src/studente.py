class student:

    def __init__(self, materia="", genere="", eta="", anno="", lezioni="", go="", info="", numero=""):
        self.materia = materia
        self.genere = genere
        self.eta = eta
        self.anno = anno
        self.lezioni = lezioni
        self.go = go
        self.info = info
        self.numero = numero

    def __str__(self):
        return f"{self.materia} ### {self.info}"