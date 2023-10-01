from django.db import models
import chess
import chess.svg
from django.core.validators import MaxValueValidator, MinValueValidator

class Puzzle(models.Model):
    position_fen = models.CharField(max_length=200)
    level = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(1)])
    label = models.CharField(max_length=200)
    prompt = models.CharField(max_length=200)
    due_date = models.DateField(null=True)
    solution = models.CharField(max_length=200)
    #week = models.IntegerField()
    #puzzle_num = models.IntegerField()


    def __str__(self):
        return self.label
    
    def position_diagram(self):
        return chess.svg.board(chess.Board(self.position_fen), size=400)
