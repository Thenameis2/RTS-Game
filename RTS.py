# # # # import pygame
# # # # import random

# # # # # Initialize Pygame
# # # # pygame.init()

# # # # # Set the dimensions of the screen
# # # # screen_width = 800
# # # # screen_height = 600
# # # # screen = pygame.display.set_mode((screen_width, screen_height))

# # # # # Set the title of the window
# # # # pygame.display.set_caption("RTS Game")

# # # # # Set the background color of the screen
# # # # bg_color = (0, 0, 0)
# # # # screen.fill(bg_color)

# # # # # Set up the font for the game text
# # # # font = pygame.font.Font(None, 24)

# # # # # Define some constants for the game
# # # # STARTING_RESOURCES = 1000
# # # # STARTING_BUILDINGS = 1
# # # # STARTING_UNITS = 10
# # # # BUILDING_COST = 100
# # # # UNIT_COST = 50

# # # # # Define a class for buildings
# # # # class Building:
# # # #     def __init__(self, x, y):
# # # #         self.x = x
# # # #         self.y = y
# # # #         self.color = (255, 0, 0)
# # # #         self.width = 50
# # # #         self.height = 50
# # # #         self.health = 100

# # # #     def draw(self):
# # # #         pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

# # # #     def is_clicked(self, mouse_pos):
# # # #         return self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height

# # # # # Define a class for units
# # # # class Unit:
# # # #     def __init__(self, x, y):
# # # #         self.x = x
# # # #         self.y = y
# # # #         self.color = (0, 255, 0)
# # # #         self.width = 20
# # # #         self.height = 20
# # # #         self.health = 100

# # # #     def draw(self):
# # # #         pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

# # # #     def move_to(self, x, y):
# # # #         self.x = x
# # # #         self.y = y

# # # # # Define a class for the game
# # # # class Game:
# # # #     def __init__(self):
# # # #         self.resources = STARTING_RESOURCES
# # # #         self.buildings = []
# # # #         self.units = []
# # # #         self.enemy_units = []
# # # #         self.enemy_buildings = []

# # # #     def draw_resources(self):
# # # #         resources_text = font.render(f"Resources: {self.resources}", True, (255, 255, 255))
# # # #         screen.blit(resources_text, (10, 10))

# # # #     def create_building(self, x, y):
# # # #         if self.resources >= BUILDING_COST:
# # # #             self.resources -= BUILDING_COST
# # # #             building = Building(x, y)
# # # #             self.buildings.append(building)

# # # #     def create_unit(self, x, y):
# # # #         if self.resources >= UNIT_COST:
# # # #             self.resources -= UNIT_COST
# # # #             unit = Unit(x, y)
# # # #             self.units.append(unit)

# # # #     def create_enemy_unit(self):
# # # #         x = random.randint(0, screen_width - 20)
# # # #         y = random.randint(screen_height // 2, screen_height - 20)
# # # #         unit = Unit(x, y)
# # # #         self.enemy_units.append(unit)

# # # #     def create_enemy_building(self):
# # # #         x = random.randint(0, screen_width - 50)
# # # #         y = random.randint(screen_height // 2, screen_height - 50)
# # # #         building = Building(x, y)
# # # #         self.enemy_buildings.append(building)

# # # #     def draw_buildings(self):
# # # #         for building in self.buildings:
# # # #             building.draw()

# # # #     def draw_units(self):
# # # #         for unit in self.units:
# # # #             unit.draw()

# # # #     def draw_enemy_units(self):
# # # #         for unit in self.enemy_units:
# # # #             unit.draw()
# # # #     def draw_enemy_buildings(self):
# # # #         for building in self.enemy_buildings:
# # # #             building.draw()

# # # #     def handle_events(self):
# # # #         for event in pygame.event.get():
# # # #             if event.type == pygame.QUIT:
# # # #                 pygame.quit()
# # # #                 quit()
# # # #             elif event.type == pygame.MOUSEBUTTONUP:
# # # #                 mouse_pos = pygame.mouse.get_pos()
# # # #                 if event.button == 1:
# # # #                     clicked_building = None
# # # #                     for building in self.buildings:
# # # #                         if building.is_clicked(mouse_pos):
# # # #                             clicked_building = building
# # # #                             break
# # # #                     if clicked_building is None:
# # # #                         self.create_unit(*mouse_pos)
# # # #                     else:
# # # #                         self.create_building(clicked_building.x + 60, clicked_building.y)

# # # #     def update(self):
# # # #         # Create enemy units and buildings
# # # #         if len(self.enemy_units) < 10:
# # # #             self.create_enemy_unit()

# # # #         if len(self.enemy_buildings) < 2:
# # # #             self.create_enemy_building()

# # # #         # Move enemy units towards player buildings
# # # #         for unit in self.enemy_units:
# # # #             closest_building = None
# # # #             closest_distance = 999999
# # # #             for building in self.buildings:
# # # #                 distance = ((unit.x - building.x)**2 + (unit.y - building.y)**2)**0.5
# # # #                 if distance < closest_distance:
# # # #                     closest_building = building
# # # #                     closest_distance = distance
# # # #             if closest_building is not None:
# # # #                 unit.move_to(closest_building.x + closest_building.width // 2 - unit.width // 2,
# # # #                             closest_building.y + closest_building.height // 2 - unit.height // 2)

# # # #         # Check for collisions between units and buildings
# # # #         for unit in self.units:
# # # #             for building in self.buildings:
# # # #                 if (unit.x + unit.width > building.x and unit.x < building.x + building.width and
# # # #                     unit.y + unit.height > building.y and unit.y < building.y + building.height):
# # # #                     self.buildings.remove(building)
# # # #                     self.units.remove(unit)

# # # #         # Check for collisions between enemy units and player buildings
# # # #         for unit in self.enemy_units:
# # # #             for building in self.buildings:
# # # #                 if (unit.x + unit.width > building.x and unit.x < building.x + building.width and
# # # #                     unit.y + unit.height > building.y and unit.y < building.y + building.height):
# # # #                     self.buildings.remove(building)
# # # #                     self.enemy_units.remove(unit)

# # # # # def run(self):
# # # # #     clock = pygame.time.Clock()
# # # # #     while True:
# # # # #         self.handle_events()
# # # # #         self.update()
# # # # #         screen.fill(bg_color)
# # # # #         self.draw_resources()
# # # # #         self.draw_buildings()
# # # # #         self.draw_units()
# # # # #         self.draw_enemy_units()
# # # # #         self.draw_enemy_buildings()
# # # # #         pygame.display.update()
# # # # #         clock.tick(60)
# # # # #         game = Game()
# # # # #         game.run()
# # # # game = Game()
# # # # clock = pygame.time.Clock()

# # # # # Game loop
# # # # while True:
# # # # # Handle events
# # # #     game.handle_events()
# # # #     game.update()

# # # # # Draw the game objects
# # # #     screen.fill(bg_color)
# # # #     game.draw_resources()
# # # #     game.draw_buildings()
# # # #     game.draw_units()
# # # #     game.draw_enemy_units()
# # # #     game.draw_enemy_buildings()
# # # #     pygame.display.update()

# # # #     # Cap the frame rate
# # # #     clock.tick(60)
# # # #     pygame.quit()
# # # import pygame

# # # # Initialize Pygame
# # # pygame.init()

# # # # Set the dimensions of the screen
# # # screen_width = 800
# # # screen_height = 600
# # # screen = pygame.display.set_mode((screen_width, screen_height))

# # # # Set the title of the window
# # # pygame.display.set_caption("RTS Game")

# # # # Set the background color of the screen
# # # bg_color = (0, 0, 0)
# # # screen.fill(bg_color)

# # # # Set up the font for the menu text
# # # font = pygame.font.Font(None, 36)

# # # # Create a menu
# # # menu_text = font.render("RTS Game Menu", True, (255, 255, 255))
# # # menu_rect = menu_text.get_rect(center=(screen_width // 2, 50))

# # # # Create a button
# # # button_text = font.render("Start Game", True, (255, 255, 255))
# # # button_rect = button_text.get_rect(center=(screen_width // 2, 150))

# # # # Create a text box
# # # text_box_rect = pygame.Rect(screen_width // 2 - 150, 250, 300, 50)
# # # text_box_color = (255, 255, 255)

# # # # Add the menu, button, and text box to the screen
# # # screen.blit(menu_text, menu_rect)
# # # screen.blit(button_text, button_rect)
# # # pygame.draw.rect(screen, text_box_color, text_box_rect, 2)

# # # # Refresh the screen
# # # pygame.display.flip()

# # # # Run the game loop
# # # running = True
# # # while running:
# # #     for event in pygame.event.get():
# # #         if event.type == pygame.QUIT:
# # #             running = False

# # #         # Check for button clicks
# # #         elif event.type == pygame.MOUSEBUTTONDOWN:
# # #             mouse_pos = pygame.mouse.get_pos()
# # #             if button_rect.collidepoint(mouse_pos):
# # #                 print("Starting game...")

# # #         # Check for text input
# # #         elif event.type == pygame.KEYDOWN:
# # #             if event.unicode.isalpha():
# # #                 print(event.unicode)

# # #     # Draw the menu, button, and text box on the screen
# # #     screen.fill(bg_color)
# # #     screen.blit(menu_text, menu_rect)
# # #     screen.blit(button_text, button_rect)
# # #     pygame.draw.rect(screen, text_box_color, text_box_rect, 2)

# # #     # Refresh the screen
# # #     pygame.display.flip()

# # # # Quit Pygame
# # # pygame.quit()
# # import pygame

# # # Initialize Pygame
# # pygame.init()

# # # Set the dimensions of the screen
# # screen_width = 800
# # screen_height = 600
# # screen = pygame.display.set_mode((screen_width, screen_height))

# # # Set the title of the window
# # pygame.display.set_caption("RTS Game")

# # # Set the background color of the screen
# # bg_color = (0, 0, 0)

# # # Set up the font for the menu text
# # font = pygame.font.Font(None, 36)

# # # Create a menu
# # menu_text = font.render("RTS Game Menu", True, (255, 255, 255))
# # menu_rect = menu_text.get_rect(center=(screen_width // 2, 50))

# # # Create a button
# # button_text = font.render("Start Game", True, (255, 255, 255))
# # button_rect = button_text.get_rect(center=(screen_width // 2, 150))

# # # Create a text box
# # text_box_rect = pygame.Rect(screen_width // 2 - 150, 250, 300, 50)
# # text_box_color = (255, 255, 255)

# # # Create a unit class
# # class Unit:
# #     def __init__(self, x, y, width, height, color):
# #         self.x = x
# #         self.y = y
# #         self.width = width
# #         self.height = height
# #         self.color = color

# #     def draw(self, surface):
# #         pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

# # # Create a list of units
# # units = [Unit(100, 100, 50, 50, (255, 0, 0)), Unit(200, 200, 50, 50, (0, 255, 0)), Unit(300, 300, 50, 50, (0, 0, 255))]

# # # Create a game loop function
# # def game_loop():
# #     # Run the game loop
# #     running = True
# #     while running:
# #         for event in pygame.event.get():
# #             if event.type == pygame.QUIT:
# #                 running = False

# #             # Check for button clicks
# #             elif event.type == pygame.MOUSEBUTTONDOWN:
# #                 mouse_pos = pygame.mouse.get_pos()
# #                 if button_rect.collidepoint(mouse_pos):
# #                     print("Starting game...")

# #             # Check for text input
# #             elif event.type == pygame.KEYDOWN:
# #                 if event.unicode.isalpha():
# #                     print(event.unicode)

# #         # Draw the menu, button, and text box on the screen
# #         screen.fill(bg_color)
# #         screen.blit(menu_text, menu_rect)
# #         screen.blit(button_text, button_rect)
# #         pygame.draw.rect(screen, text_box_color, text_box_rect, 2)

# #         # Draw the units on the screen
# #         for unit in units:
# #             unit.draw(screen)

# #         # Refresh the screen
# #         pygame.display.flip()

# #     # Quit Pygame
# #     pygame.quit()

# # # Start the game loop
# # game_loop()
# import speech_recognition as sr
# import os
# from gtts import gTTS
# from PyQt5 import QtWidgets, QtCore, QtGui
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QTextEdit

# class VirtualAssistant(QMainWindow):
#     def __init__(self):
#         super(VirtualAssistant, self).__init__()

#         self.setWindowTitle("Virtual Assistant")
#         self.setGeometry(100, 100, 500, 500)

#         self.initUI()

#     def initUI(self):
#         self.label = QLabel("Welcome to Virtual Assistant", self)
#         self.label.move(100, 50)
#         self.label.resize(300, 50)
#         self.label.setAlignment(QtCore.Qt.AlignCenter)

#         self.text_box = QTextEdit(self)
#         self.text_box.move(100, 130)
#         self.text_box.resize(300, 100)

#         self.button = QPushButton("Speak", self)
#         self.button.move(200, 250)
#         self.button.resize(100, 50)
#         self.button.clicked.connect(self.process_input)

#     def process_input(self):
#         recognizer = sr.Recognizer()
#         with sr.Microphone() as source:
#             recognizer.adjust_for_ambient_noise(source)
#             audio = recognizer.listen(source)

#         try:
#             text = recognizer.recognize_google(audio)
#             self.text_box.setText(text)
#             self.perform_action(text)
#         except:
#             self.text_box.setText("Sorry, I could not understand you")

#     def perform_action(self, text):
#         if "hello" in text.lower():
#             self.say("Hello, how can I help you?")
#         elif "what is the time" in text.lower():
#             import datetime
#             time = datetime.datetime.now().strftime("%I:%M %p")
#             self.say(f"The time is {time}")
#         elif "what is your name" in text.lower():
#             self.say("My name is Virtual Assistant")

#     def say(self, text):
#         speech = gTTS(text=text)
#         speech.save("output.mp3")
#         os.system("mpg321 output.mp3")

# if __name__ == "__main__":
#     app = QApplication([])
#     window = VirtualAssistant()
#     window.show()
#     app.exec_()

# import tkinter as tk
# from tkinter import ttk
# import tensorflow as tf

# class Application(tk.Tk):
#     def __init__(self, model, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.model = model
#         self.title("AI Chatbot")
#         self.geometry("400x300")
#         self.resizable(False, False)

#         # Create the input and output widgets
#         input_frame = ttk.Frame(self)
#         input_frame.pack(padx=10, pady=10, fill="x")
#         ttk.Label(input_frame, text="Enter your question:").pack(side="left", padx=5, pady=5)
#         self.input_entry = ttk.Entry(input_frame)
#         self.input_entry.pack(side="left", fill="x", expand=True)

#         output_frame = ttk.Frame(self)
#         output_frame.pack(padx=10, pady=10, fill="both", expand=True)
#         ttk.Label(output_frame, text="Answer:").pack(side="left", anchor="nw", padx=5, pady=5)
#         self.output_text = tk.Text(output_frame, wrap="word", state="disabled")
#         self.output_text.pack(side="left", fill="both", expand=True)

#         # Create the "Ask" button
#         ttk.Button(self, text="Ask", command=self.ask).pack(padx=10, pady=10)

#     def ask(self):
#         # Get the user input
#         user_input = self.input_entry.get()
#         self.input_entry.delete(0, "end")

#         # Generate a response using the model
#         response = self.model.generate_response(user_input)

#         # Update the output text widget
#         self.output_text.configure(state="normal")
#         self.output_text.delete(1.0, "end")
#         self.output_text.insert("end", response)
#         self.output_text.configure(state="disabled")

# if __name__ == "__main__":
#     # Define and train the model
#     import tensorflow as tf
#     model = tf.keras.models.Sequential([
#         # Define your model architecture here
#     ])
#     model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
#     inputs = ['What is the capital of France?', 'Who invented the telephone?', 'What is the meaning of life?']
#     outputs = ['Paris', 'Alexander Graham Bell', '42']
#     model.fit(inputs, outputs, epochs=100)

#     # Create and run the GUI application
#     app = Application(model)
#     app.mainloop()
# import openai
# import PySimpleGUI as sg

# # Authenticate with OpenAI API
# openai.api_key = "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"

# # Define a function to generate responses from OpenAI API
# def generate_response(prompt):
#     response = openai.Completion.create(
#         engine="davinci",
#         prompt=prompt,
#         max_tokens=60,
#         n=1,
#         stop=None,
#         temperature=0.7,
#     )
#     return response.choices[0].text.strip()

# # Define GUI layout
# layout = [
#     [sg.Text("AI Chatbot")],
#     [sg.Multiline(size=(50, 10), key="-INPUT-")],
#     [sg.Button("Send"), sg.Button("Exit")],
#     [sg.Text(size=(50, 10), key="-OUTPUT-")],
# ]

# # Create GUI window
# window = sg.Window("AI Chatbot", layout)

# # Event loop to process "Send" and "Exit" buttons
# while True:
#     event, values = window.read()
#     if event == sg.WINDOW_CLOSED or event == "Exit":
#         break
#     if event == "Send":
#         input_text = values["-INPUT-"].strip()
#         if input_text:
#             response = generate_response(input_text)
#             window["-OUTPUT-"].update(response)

# # Close GUI window
# window.close()
import chatterbot
from chatterbot.trainers import ChatterBotCorpusTrainer
import PySimpleGUI as sg

# Create and train chatbot
chatbot = chatterbot.ChatBot('My ChatBot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Define GUI layout
layout = [
    [sg.Text("AI Chatbot")],
    [sg.Multiline(size=(50, 10), key="-INPUT-")],
    [sg.Button("Send"), sg.Button("Exit")],
    [sg.Text(size=(50, 10), key="-OUTPUT-")],
]

# Create GUI window
window = sg.Window("AI Chatbot", layout)

# Event loop to process "Send" and "Exit" buttons
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    if event == "Send":
        input_text = values["-INPUT-"].strip()
        if input_text:
            response = chatbot.get_response(input_text)
            window["-OUTPUT-"].update(str(response))

# Close GUI window
window.close()
