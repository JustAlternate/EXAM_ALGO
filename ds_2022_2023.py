from __future__ import annotations
import random
from math import sqrt

"""
J'aurais peut-être dû inclure le père noel dans la liste de Lutins ça facilite pas le fait de passer un message par défaut
"""


def pi(n=0, deno=1):
    if n != 0:
        deno = sqrt(2 + (deno if deno != 1 else 0))

    if (2 / deno) <= (1 + 10**-15):
        return 1

    return (2 / deno) * pi(n + 1, deno)


PI = pi()


def is_perfect(n):
    sum = 1
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            if i * (n // i) == n:
                sum += i + n // i
            i += 1
    return sum == n and n != 1


class Pere_Noel:
    def __init__(self, message: str = "Joyeux noël"):
        self.message = message
        self.lutins = Lutins()
        self.messager = None

    def ajout_messager(self, prenom: str):
        if self.messager is None:
            self.lutins.ajout_lutin(prenom)
            self.messager = self.lutins.premier_lutin
            self.messager.recoit_msg(self)


class Lutins:
    def __init__(self) -> None:
        self.premier_lutin = None

    def isEmpty(self) -> bool:
        return self.premier_lutin is None

    def ajout_lutin(
        self, prenom: str
    ) -> None:  # Fonctionne que lorsque l'on a déjà le premier lutin
        lutin = Lutin(prenom, age=round(1 * PI))

        if self.premier_lutin is None:
            self.premier_lutin = lutin
        else:
            current = self.premier_lutin

            age = 2
            while current.lutin_suiv:
                age += 1
                current = current.lutin_suiv

            lutin.age = round(age * PI)
            lutin.recoit_msg(current)
            current.lutin_suiv = lutin

    def afficher(self) -> None:
        if not self.isEmpty():
            current = self.premier_lutin
            while current:
                print(current)
                current = current.lutin_suiv

    def lutins_parfait(self) -> list:
        lutins = []

        current = self.messager
        while current:
            if current.parfait:
                lutins.append(current)

            current = current.lutin_suiv

        return lutins

    def dernier_message(self) -> str:
        return f"Dernier message : {self.premier_lutin.message_lutin()}"


class Lutin:
    def __init__(self, prenom: str, age: int = 100):
        self.prenom: str = prenom
        self.age: int = age

        self.niv_audition: int = random.randint(-5, 5)
        self.nb_kdo_fab: int = random.randint(0, 100)
        self.nb_kdo_emba: int = random.randint(0, 100)

        self.lutin_prec: Lutin = None
        self.lutin_suiv: Lutin = None
        self.message: str = None
        self.parfait = self.est_parfait()

    def est_parfait(self):
        return is_perfect(self.nb_kdo_emba) and is_perfect(self.nb_kdo_fab)

    def recoit_msg(self, instance: Pere_Noel | Lutin) -> None:
        if isinstance(instance, Pere_Noel) or isinstance(instance, Lutin):
            modif = abs(self.niv_audition)
            message = list(instance.message)
            for i in range(modif):
                val = message.pop(0)
                message.append(val)
            self.message = "".join(message)
        else:
            print(
                "Un lutin ne peut recevoir un message que du Pere Noël ou d'un camarade lutin"
            )

    def message_lutin(self):
        if self.lutin_suiv == None:
            return self.message
        else:
            return self.lutin_suiv.message_lutin()

    def __str__(self):
        chaine = f"Lutin - {self.prenom} :\n"
        chaine += f"- Age : {self.age}\n"
        chaine += f"- Niveau audition : {self.niv_audition}\n"
        chaine += f"- Nombre de cadeaux fabriqués : {self.nb_kdo_fab}\n"
        chaine += f"- Nombre de cadeaux emballés : {self.nb_kdo_emba}\n"
        chaine += f"- Message : {self.message}\n"
        chaine += f"- Parfait : {self.parfait}\n"

        return chaine


Santa = Pere_Noel()
Santa.ajout_messager("Bob")
Santa.lutins.ajout_lutin("Tom")
Santa.lutins.ajout_lutin("Timoté")

Santa.lutins.afficher()
print(Santa.lutins.dernier_message())
