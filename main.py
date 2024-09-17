from dices.regular_dice import create_regular_six_sided_dice
from dices.dice import Dice
 
#########################################################
# Ska rensas
def throw(dices:list[Dice]) -> None:
    for dice in dices:
        dice.roll()
 
def draw_dices_horizontal(dices:list[Dice]) -> str:
    d = [dice.side_up.face.get_face() for dice in dices]
    dice_string = ''
    for row in range(len(d[0])):
        for dice in d:
            dice_string += dice[row] + ' '
 
        dice_string += '\n'
   
    return dice_string
#########################################################
 
def main():
    five_dices = [create_regular_six_sided_dice() for _ in range(5)]
    throw(five_dices)    
    print(draw_dices_horizontal(five_dices))
    numbers = {"ONE": 1, "TWO": 2, "THREE": 3, "FOUR": 4, "FIVE": 5, "SIX": 6}
    saved_result = []
    temp_result = []
    for dice in five_dices:
        temp_result.append(numbers[str(dice._side_up._value).split(".",1)[1]])
    rerolls = ["1", "2", "3", "4", "5"]
    val_1 = input("Vänligen skriv vilka tärningar du vill spara och tryck sedan enter för att avsluta\n")
    for siffra in val_1:
        if siffra in rerolls:
            rerolls.remove(siffra)
            saved_result.append(temp_result[int(siffra)-1])
    if len(rerolls):
        round_2 = [create_regular_six_sided_dice() for i in range(len(rerolls))]
        throw(round_2)
        print(draw_dices_horizontal(round_2))  
        rerolls = [str(i) for i in range(1, len(rerolls)+1)]
        temp_result = []
        for dice in round_2:
            temp_result.append(numbers[str(dice._side_up._value).split(".",1)[1]])
        print("Saved dice: " + str(saved_result))
        val_2 = input("Vänligen skriv vilka tärningar du vill spara och tryck sedan enter för att avsluta\n")
        for siffra in val_2:
            if siffra in rerolls:
                rerolls.remove(siffra)
                saved_result.append(temp_result[int(siffra)-1])
        if len(rerolls):
            rerolls = [str(i) for i in range(1, len(rerolls))]
            round_3 = [create_regular_six_sided_dice() for _ in range(len(rerolls)+1)]
            throw(round_3)
            print(draw_dices_horizontal(round_3))  
            temp_result = []
            for dice in round_3:
                temp_result.append(numbers[str(dice._side_up._value).split(".",1)[1]])
            poäng = 0
            for value in saved_result:
                poäng += value
            for value in temp_result:
                poäng += value
            print("Saved dice: " + str(saved_result))
            print("Du fick " + str(poäng)+ " poäng!")
            exit()
        else:
            poäng = 0
            for value in saved_result:
                poäng += value
            for value in temp_result:
                poäng += value
            print("Saved dice: " + str(saved_result))
            print("Du fick " + str(poäng)+ " poäng!")
            exit()
    else:
        poäng = 0
        for value in temp_result:
            poäng += value
        print("Saved dice: " + str(saved_result))
        print("Du fick " + str(poäng)+ " poäng!")
        exit()
 
if __name__ == '__main__':
    main()