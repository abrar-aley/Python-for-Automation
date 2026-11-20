
import math

def sine(angle):
    return math.sin(math.radians(angle))


def cosine(angle):
    return math.cos(math.radians(angle))


def tangent(angle):
    return math.tan(math.radians(angle))


def cosecant(angle):
    return 1 / sine(angle)


def secant(angle):
    return 1 / cosine(angle)


def cotangent(angle):
    return 1 / tangent(angle)


def degrees_to_radians(angle):
    return math.radians(angle)


def radians_to_degrees(angle):
    return math.degrees(angle)
