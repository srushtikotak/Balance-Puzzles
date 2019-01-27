import turtle
"""
CSCI-603: LAB 8  

This program reads a balance puzzle from a file and verifies it and draws it.
Authors: Srushti Kotak
"""


class Beam:
    """
    This class creates a beam object that contains data
    """
    __slots__ = 'beam'

    def __init__(self, beam):
        """
        Constructor of Beam class
        :param beam: dictionary of distance : weight objects
        """
        self.beam = {}
        self.create(beam)

    def create(self, beam):
        """
        creates a beam object
        :param beam: dictionary of distance : weight objects
        :return: beam object
        """
        b_name = beam[0]
        beam = beam[1:]
        index = 0
        while (index + 1) <= (len(beam) - 1):
            self.beam["b_name"] = b_name
            self.beam[beam[index]] = beam[index+1]
            index += 2
        return beam

    def left_right(beam):
        """
        Computes the left and right extent of a beam
        """
        b_name = beam[0]
        beam = beam[1:]
        left = beam[0]
        right = beam[len(beam) - 2]
        print("Left extent of " + b_name + " is " + str(abs(int(left))) +
              " and Right extent of " + b_name + " is " + str(abs(int(right))))
        print("Length of " + b_name + " is " + str(abs(int(left)) + abs(int(right))))

    def weight(beam):
        """
         Computes the total weight of a beam
        :return: total weight of the beam
        """
        total_weight = 0
        for i in beam:
            if i != "b_name":
                total_weight += int(beam[i])
        return total_weight

    def draw(self, beams_list, beams_name, t, scale, weight):
        """
        The function draws the balance puzzle with the help of turtle
        :param beams_list: dictionary of beams
        :param beams_name: list of beams
        :param t: turtle
        :param weight: object of Weight class
        :return: None
        :pre: pos (0,0) relative, heading (east), up
        :post: pos (0,0) relative, heading (east), up
        """
        height = 40
        beams_list = beams_list[::-1]
        t.penup()
        t.right(90)
        t.pendown()
        t.forward(height)
        t.penup()
        t.left(90)
        for i in range(len(beams_list)):
            for j in beams_list[i]:
                if j != 'b_name':
                    t.pendown()
                    t.forward(int(j) * scale)
                    t.penup()
                    # recursive call to draw beams in beams
                    if beams_list[i][j] in beams_name:
                        self.draw([beams_name.get(beams_list[i][j])], beams_name, t, scale / 2.5, weight)
                        t.penup()
                        t.left(90)
                        t.forward(height)
                        t.right(90)
                        t.backward((int(j) * scale))
                    else:
                        if beams_list[i][j] == '-1':
                            beams_list[i][j] = str(weight.balance_wt)
                        t.left(90)
                        t.pendown()
                        t.forward(-height)
                        t.penup()
                        # writing space
                        t.forward(-30)
                        t.pendown()
                        t.write(beams_list[i][j], font=("Arial", 15, "bold"))
                        t.penup()
                        t.forward(height + 30)
                        t.right(90)
                        t.backward((int(j) * scale))
            break


class Weight:
    """
    Weight class is used to check if the beams are balanced and if not balanced,
    compute the balance weight and update it
    """
    __slots__ = 'beams_list', 'beams_name', 'balance_wt'

    def __init__(self, beams_list, beams_name):
        """
        Constructor
        :param beams_list: dictionary of beams
        :param beams_name: list of beams
        """
        self.beams_list = beams_list
        self.beams_name = beams_name
        self.balance_wt = 0
        self.balance()

    def balance(self):
        """
        function to check if the beams are balanced and if not balanced,
        compute the balance weight and update it
        :return: None
        """
        for i in range(len(self.beams_list)):
            balance_torque = 0
            for j in self.beams_list[i]:
                if j != 'b_name':
                    if self.beams_list[i][j] in self.beams_name:
                        self.beams_list[i][j] = Beam.weight(self.beams_name.get(self.beams_list[i][j]))

                    if int(self.beams_list[i][j]) == -1:
                        print("Beam " + str(self.beams_list[i]['b_name']) + " has an empty pan ")
                        for k in self.beams_list[i]:
                            if k != 'b_name' and self.beams_list[i][k] != '-1':
                                balance_torque += int(k) * int(self.beams_list[i][k])

                        self.balance_wt = balance_torque = str(abs(-balance_torque // int(j)))
                        self.beams_list[i][j] = balance_torque
                        print("Empty pan in " + str(self.beams_list[i]['b_name']) + " is filled with "
                                + "weight " + str(balance_torque) + " to balance the puzzle")

            l_torque = r_torque = 0
            for k in self.beams_list[i]:
                if k != 'b_name' and self.beams_list[i][k] != '-1':
                    if int(k) < 0:
                        l_torque += int(k) * int(self.beams_list[i][k])
                    else:
                        r_torque += int(k) * int(self.beams_list[i][k])

            if abs(l_torque) == abs(r_torque):
                print(str(self.beams_list[i]['b_name']) + " is balanced")
            else:
                print(str(self.beams_list[i]['b_name']) + " is not balanced")


def main():
    """
    Main function
    :return: None
    """
    file = input("Enter the name of the file with balance puzzle : ")
    beams_list = []
    beams_name = {}
    for line in open(file):
        line = line.split()
        beam = Beam(line)
        beams_list.append(beam.beam)
        beams_name[line[0]] = beam.beam
        Beam.left_right(line)
    weight = Weight(beams_list, beams_name)
    for line in open(file):
        line = line.split()
        beam = Beam(line)
        beams_list.append(beam.beam)
        beams_name[line[0]] = beam.beam
    beam.draw(beams_list, beams_name, turtle, 100, weight)
    turtle.exitonclick()


if __name__ == '__main__':
    main()
