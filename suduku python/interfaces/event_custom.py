import pygame

MY_CUSTOM_EVENT = pygame.USEREVENT + 1


def post_custom_event():
    pygame.event.post(pygame.event.Event(MY_CUSTOM_EVENT))
