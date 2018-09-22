import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from game_stats import GameStats
from button import Button


def run_game():
    # Initialize pygame, settings and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the Play button
    play_button = Button(ai_settings, screen, "Play")

    # Make a ship.
    ship = Ship(ai_settings, screen)

    # Make a group to store bullets in.
    bullets = Group()

    # Make an alien.
    # alien = Alien(ai_settings, screen)

    # Make many aliens
    aliens = Group()

    # Create fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Create an instance to store game settings
    stats = GameStats(ai_settings)

    # Set background color.
    bg_color = (230, 230, 230)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)


run_game()

