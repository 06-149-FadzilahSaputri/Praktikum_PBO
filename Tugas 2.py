#123140149_Fadzilah-Saputri_PBO-RA
#Tugas2

import random
import time

class Robot:
    def __init__(self, name, attack, hp, accuracy):
        """Inisialisasi Robot dengan atribut dasar."""
        self.name = name  
        self.attack = attack  
        self.hp = hp  
        self.accuracy = accuracy #0-100% 
        self.status_effects = [] #stun, silence, dll  

    def attack_enemy(self, enemy):
        """Menyerang robot lawan jika tidak terkena stun atau silence."""
        if "stunned" in self.status_effects:
            print(f"{self.name} tidak bisa menyerang karena terkena Stun!")
            return
        if "silenced" in self.status_effects:
            print(f"{self.name} tidak bisa menggunakan skill karena terkena Silence!")
            return
        #menentukan apakah serangan berhasil atau tidak berdasarkan akurasi
        if random.randint(1, 100) <= self.accuracy:
            damage = random.randint(self.attack - 2, self.attack + 2)  
            enemy.hp -= damage  #damage yg diterima oleh musuh (mengurangi hp-nya)
            print(f"{self.name} menyerang {enemy.name} dan memberikan {damage} damage!")
        else:
            print(f"{self.name} meleset dalam menyerang {enemy.name}!")

    def regen_health(self):
        """Memulihkan sebagian HP."""
        heal = random.randint(5, 10)
        self.hp += heal
        print(f"{self.name} memulihkan {heal} HP!")

    def apply_status_effects(self, enemy):
        """Menerapkan efek status secara acak pada musuh."""
        if random.random() < 0.3:  #30% kemungkinan memberikan efek status
            effect = random.choice(["stunned", "silenced"])
            enemy.status_effects.append(effect)
            print(f"{self.name} memberikan efek {effect} pada {enemy.name}!")

    def remove_status_effects(self):
        """Menghapus efek status setelah 1 ronde."""
        self.status_effects = [] #jika kita terkena serangan effect akan hilang setelah menyelesaikan 1 ronde

class Game:
    def __init__(self, robot1, robot2):
        """Mengatur jalannya permainan dengan dua robot."""
        self.robot1 = robot1
        self.robot2 = robot2
        self.round = 1  #ronde dimulai dari 1 

    def play(self):
        """Menjalankan permainan sampai salah satu robot kalah."""
        while self.robot1.hp > 0 and self.robot2.hp > 0: #jika salah satu robot kalah maka permainan akan berhenti
            print(f"\n===== Ronde {self.round} =====")
            print(f"{self.robot1.name}: {self.robot1.hp} HP || {self.robot2.name}: {self.robot2.hp} HP")

            print(f"\nGiliran {self.robot1.name}:") #pemain atau user dapat memilih aksi
            self.player_action(self.robot1, self.robot2)

            if self.robot2.hp <= 0:
                print(f"{self.robot2.name} kalah! {self.robot1.name} memenangkan pertarungan!")
                break 

            print(f"\nGiliran {self.robot2.name}:")
            self.player_action(self.robot2, self.robot1)

            if self.robot1.hp <= 0:
                print(f"{self.robot1.name} kalah! {self.robot2.name} memenangkan pertarungan!")
                break

            self.robot1.remove_status_effects()
            self.robot2.remove_status_effects()

            self.round += 1  
            time.sleep(1)  

    def player_action(self, attacker, defender):
        """Memungkinkan pemain memilih tindakan untuk robot mereka."""
        print("Pilih aksi:")
        print("1. Serang")
        print("2. Pulihkan HP")
        print("3. Beri efek status pada musuh")
        
        choice = input("Masukkan pilihan (1/2/3): ")
        if choice == "1":
            attacker.attack_enemy(defender)
        elif choice == "2":
            attacker.regen_health()
        elif choice == "3":
            attacker.apply_status_effects(defender)
        else:
            print("Pilihan tidak valid, serangan otomatis dilakukan.")
            attacker.attack_enemy(defender)

robot1 = Robot("Mecha-X", attack=10, hp=50, accuracy=80)
robot2 = Robot("Robo-Z", attack=12, hp=50, accuracy=75)

game = Game(robot1, robot2)
game.play()