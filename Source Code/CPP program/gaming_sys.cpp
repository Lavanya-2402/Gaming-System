#include <graphics.h>
#include <conio.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>

// Global variables
int mode = 1, target, scale;
char targetstr[3], scalestr[3], p1name[20], p2name[20];

// Function to display the home screen
int home()
{
    // Clear the graphics screen
    cleardevice();

    // Variable declarations
    int ch;
    char inp;

    // Drawing the border
    setfillstyle(6, 7);
    rectangle(0, 0, getmaxx(), getmaxy());
    rectangle(0 + 20, 0 + 20, getmaxx() - 20, getmaxy() - 20);
    floodfill(1, 1, 15);

    // Displaying the title
    settextstyle(0, 0, 5);
    outtextxy(65, 60, "Gaming system");

    // Displaying the description
    settextstyle(8, 0, 1);
    outtextxy(30, 100, "Count Crusade refers to a mission or an effort to reach");
    outtextxy(30, 120, " a numerical target by counting or adding numbers. It");
    outtextxy(30, 140, "suggests a journey or a battle to achieve a goal through");
    outtextxy(60, 160, " the use of numbers and mathematical operations. ");

    // Prompting the user
    outtextxy(190, 200, "Press the appropriate key");

    // Drawing the "Play" option
    setfillstyle(1, 2);
    bar3d(198, 260, 398, 300, 5, 1);
    floodfill(199, 261, 15);
    settextstyle(3, 0, 1);
    outtextxy(250, 265, "P - Play");

    // Drawing the "Tutorial" option
    setfillstyle(1, 9);
    bar3d(198, 330, 398, 370, 5, 1);
    floodfill(199, 331, 15);
    outtextxy(250, 336, "T = Tutorial");

    // Drawing the "Quit" option
    setfillstyle(1, 4);
    bar3d(198, 400, 398, 440, 5, 1);
    floodfill(199, 401, 15);
    outtextxy(250, 403, "Q - Quit");

    // Get user input
    ch = getch();

    // Return the user's choice
    return ch;
}


int tutorial()
{
    cleardevice();
    int ch = 66;
    while (1)
    {
        // first page
        if (ch == 98 || ch == 66)
        {
            cleardevice();
            // border
            setfillstyle(6, 7);
            rectangle(0, 0, getmaxx(), getmaxy());
            rectangle(0 + 20, 0 + 20, getmaxx() - 20, getmaxy() - 20);
            floodfill(1, 1, 15);

            setcolor(CYAN);
            settextstyle(0, 0, 5);
            outtextxy(90, 60, "How to play");

            // Displaying game setup information
            settextstyle(3, 0, 3);
            setcolor(15);
            outtextxy(40, 125, "Assume:");
            outtextxy(40, 145, "Target: 20");
            outtextxy(40, 170, "Scale: 1-6");
            outtextxy(40, 195, "Players: 2");
            outtextxy(40, 215, "Operation: addition(+)");

            // Rule 1
            setcolor(14);
            outtextxy(40, 270, "1. Player-1 move must be in a scale of 1 - 6.");
            setcolor(GREEN);
            rectangle(30, 305, 300, 330);
            outtextxy(40, 300, "PLAYER - 1 move : 5");

            // Rule 2
            setcolor(14);
            outtextxy(40, 350, "2. Player-2 move must be in a scale of 5 - 11.");
            outtextxy(30, 370, "any number from 6(5+1) to 11 (5+6) as scale=6.");
            setcolor(GREEN);
            rectangle(30, 405, 310, 435);
            outtextxy(40, 400, "PLAYER - 2 move : 11");

            // Navigation instructions
            setcolor(RED);
            outtextxy(500, 400, "N");
            setcolor(WHITE);
            outtextxy(520, 400, "-Next");

            setcolor(RED);
            outtextxy(500, 425, "H");
            setcolor(WHITE);
            outtextxy(520, 425, "-Home");

            // Waiting for user input
            while (1)
            {
                if (kbhit())
                {
                    ch = getch();
                    break;
                }
            }
        }

        // second page
        if (ch == 110 || ch == 78)
        {
            cleardevice();
            // border
            setfillstyle(6, 7);
            rectangle(0, 0, getmaxx(), getmaxy());
            rectangle(0 + 20, 0 + 20, getmaxx() - 20, getmaxy() - 20);
            floodfill(1, 1, 15);
            
            // Rule 3
            settextstyle(3, 0, 3);
            setcolor(14);
            outtextxy(40, 40, "3. Player-1 move must be in a scale of 12 - 17.");
            outtextxy(30, 60, "Any no. from 12 (11+1) to 17 (11+6) as scale=6.");
            setcolor(GREEN);
            rectangle(30, 95, 310, 120);
            outtextxy(40, 90, "PLAYER - 1 move : 16");

            // Rule 4
            setcolor(14);
            outtextxy(40, 140, "4. Player-2 move must be in a scale of 16 - 20.");
            outtextxy(30, 160, "Any no. from 16 (15+1) to 20 as scale=6 and ");
            outtextxy(30, 180, "target=20.");
            setcolor(GREEN);
            rectangle(30, 215, 310, 245);
            outtextxy(40, 210, "PLAYER - 2 move : 20");

            // Result and options
            outtextxy(200, 270, "PLAYER - 2 wins!");
            setcolor(RED);
            outtextxy(500, 350, "B");
            setcolor(WHITE);
            outtextxy(520, 350, "-Back");

            setcolor(RED);
            outtextxy(500, 375, "Q");
            setcolor(WHITE);
            outtextxy(520, 375, "-Quit");

            setcolor(RED);
            outtextxy(500, 400, "H");
            setcolor(WHITE);
            outtextxy(520, 400, "-Home");

            // Waiting for user input
            while (1)
            {
                if (kbhit())
                {
                    ch = getch();
                    break;
                }
            }
        }

        // home
        if (ch == 72 || ch == 104)
        {
            return 72;
        }

        // quit
        else
        {
            cleardevice();
            if (kbhit())
                exit(1);
        }
    }
}


void setgame()
{
    cleardevice();

    setcolor(15);
    rectangle(0, 0, getmaxx(), getmaxy());
    rectangle(0 + 20, 0 + 20, getmaxx() - 20, getmaxy() - 20);

    int x = 100, y = 100, i = 0;

    setfillstyle(10, 9);
    floodfill(31, 31, 15);

    settextstyle(3, 0, 5);
    outtextxy(x, y, "Enter the target: ");
    // char d[1];
    // while ((targetstr[i] = getch()) != '\r')
    // {
    //  d[0] = targetstr[i];
    //  i++;
    //  outtextxy(x + 360 + i * 20, y + 30, d);
    // }
    // target = strtol(targetstr, NULL, 10);
    scanf("%d", &target);
    sprintf(targetstr, "%d", target);
    outtextxy(x + 360, y, targetstr);
    outtextxy(x - 20, y + 60, "Enter the scale(1-?): ");
    scanf("%d", &scale);
    sprintf(scalestr, "%d", scale);
    outtextxy(x + 420, y + 60, scalestr);

    setcolor(1);
    outtextxy(x - 10, y + 120, "Enter player-1 name: ");
    // scanf("%s", p1name);
    char c[1];
    while ((p1name[i] = getch()) != '\r')
    {
        c[0] = p1name[i];
        i++;
        outtextxy(x + 100 + i * 20, y + 170, c);
    }
    if (mode == 1)
    {
        int j = 0;
        setcolor(3);
        outtextxy(x - 10, y + 220, "Enter player-2 name: ");
        // scanf("%s", p2name);
        while ((p2name[j] = getch()) != '\r')
        {
            c[0] = p2name[j];
            outtextxy(x + 100 + j * 20, y + 270, c);
            j++;
        }
        outtextxy(x + 100, y + 270, p2name);
    }
}

void display(char *p1, char *p2, int flag)
{
    cleardevice();

    int ch;

    // border
    setcolor(9);
    rectangle(0, 0, getmaxx(), getmaxy());
    rectangle(0 + 10, 0 + 10, getmaxx() - 10, getmaxy() - 10);

    setbkcolor(0);

    setcolor(WHITE);
    settextstyle(3, 0, 3);
    outtextxy(100, 180, p1name);

    if (mode == 2)
        outtextxy(430, 180, "Computer");
    else
        outtextxy(430, 180, p2name);

    settextstyle(1, 0, 7);
    outtextxy(80, 50, "BATTLE GROUND");

    setcolor(3);
    rectangle(70, 150, 230, 330);
    rectangle(75, 155, 225, 325);
    outtextxy(110, 230, p1);

    setcolor(6);
    rectangle(400, 150, 560, 330);
    rectangle(405, 155, 555, 325);
    outtextxy(440, 230, p2);

    setcolor(15);
    settextstyle(1, 0, 5);
    // valid input
    if (flag == 1)
    {
        outtextxy(160, 350, "TARGET = ");
        outtextxy(380, 350, targetstr);
        outtextxy(160, 390, "SCALE = ");
        outtextxy(360, 390, "1 - ");
        outtextxy(460, 390, scalestr);
    }
    // player-1 invalid input
    if (flag == 2)
    {
        outtextxy(90, 350, p1name);
        outtextxy(280, 350, "Invalid input !");
        if (mode == 2)
            outtextxy(140, 390, "Computer");
        else
            outtextxy(140, 390, p2name);
        outtextxy(360, 390, "Won !");
    }
    // player-2 invalid input
    if (flag == 3)
    {
        outtextxy(90, 350, p2name);
        outtextxy(280, 350, "Invalid input !");
        outtextxy(140, 390, p1name);
        outtextxy(360, 390, "Won !");
    }
    // player-1 wins
    if (flag == 4)
    {
        outtextxy(140, 350, p1name);
        outtextxy(360, 350, "Won !");
    }

    // player-2 wins
    if (flag == 5)
    {
        if (mode == 2)
            outtextxy(140, 350, "Computer");
        else
            outtextxy(140, 350, p2name);
        outtextxy(360, 350, "Won !");
    }
    if (flag == 2 || flag == 3 || flag == 4 || flag == 5)
    {
        settextstyle(3, 0, 3);
        setcolor(2);
        outtextxy(80, 435, "Press any key to exit");
        getch();
        exit(1);
    }
}

int valid(int x, int sum, int id)
{
    if (sum - x >= 1 && sum - x <= scale && sum <= target)
        return 1;
    else
    {
        if (id == 1)
            return 2;
        else
            return 3;
    }
    return 1;
}
int won(int x)
{
    if (x == target)
        return 1;
    else
        return 0;
}

void play()
{
    int player_1, player_2;
    char p1s[3] = "0", p2s[3] = "0";
    display(p1s, p2s, 1);

    // player-1 input
    scanf("%d", &player_1);
    sprintf(p1s, "%d", player_1);
    display(p1s, p2s, 1);

    if (player_1 < 1 || player_1 > scale)
    {
        display(p1s, p2s, 2);
    }

    while (1)
    {
        // player-2 input
        if (mode == 1)
        {
            scanf("%d", &player_2);
            sprintf(p2s, "%d", player_2);
            display(p1s, p2s, 1);
        }
        if (mode == 2)
        {
            if (player_1 + scale >= target)
                player_2 = target;
            else
            {
                srand(time(NULL));
                player_2 = rand() % scale + player_1 + 1;
                sprintf(p2s, "%d", player_2);
                display(p1s, p2s, 1);
            }
        }
        if (valid(player_1, player_2, 1) == 2)
            display(p1s, p2s, 3);

        if (won(player_2))
        {
            display(p1s, p2s, 5);
        }

        // player-1 input
        scanf("%d", &player_1);
        sprintf(p1s, "%d", player_1);
        display(p1s, p2s, 1);

        if (valid(player_2, player_1, 2) == 3)
            display(p1s, p2s, 2);

        if (won(player_1))
        {
            display(p1s, p2s, 4);
        }
    }
}
int rules()
{
    cleardevice();
    // border
    // setfillstyle(6, 7);
    rectangle(0, 0, getmaxx(), getmaxy());
    rectangle(0 + 20, 0 + 20, getmaxx() - 20, getmaxy() - 20);
    // floodfill(5, 5, 15);

    setbkcolor(9);
    setcolor(2);
    settextstyle(0, 0, 4);
    outtextxy(230, 50, "RULES");

    settextstyle(1, 0, 2);
    setcolor(15);
    int x = 40, y = 100;
    outtextxy(x, y, "1. The objective of the game is to reach a target");
    outtextxy(x, y + 30, "number by adding numbers within the scale to the ");
    outtextxy(x, y + 60, "previous input.");
    outtextxy(x, y + 90, "2. The player starts by inputting a number");
    outtextxy(x, y + 120, "within the scale.");
    outtextxy(x, y + 150, "3. In each turn, the player must add a new number");
    outtextxy(x, y + 180, "within the scale to the previous input.");
    outtextxy(x, y + 210, "4. The game ends when the target is reached or when");
    outtextxy(x, y + 240, "the player's move is invalid (out of scale).");
    outtextxy(x, y + 270, "5. You've press enter after each move.");
    setcolor(2);
    settextstyle(0, 0, 3);
    outtextxy(x + 10, y + 300, "Press any key to start");

    getch();
    cleardevice();
    return 1;
}

int choice()
{
    cleardevice();

    // border
    setfillstyle(1, 12);
    rectangle(0, 0, getmaxx(), getmaxy());
    rectangle(0 + 20, 0 + 20, getmaxx() - 20, getmaxy() - 20);
    floodfill(1, 1, 15);

    setfillstyle(10, 4);
    floodfill(30, 311, 15);

    settextstyle(0, 0, 5);
    setcolor(15);
    outtextxy(140, 50, "play with");
    settextstyle(1, 0, 3);
    setcolor(3);
    outtextxy(170, 100, "Press the approriate key");
    int r;
    for (r = 100; r >= 90; r--)
    {
        setcolor(14);
        arc(180, 250, 0, 360, r);
    }
    settextstyle(8, 0, 3);
    outtextxy(130, 230, "F-Friends");
    for (r = 100; r >= 90; r--)
    {
        arc(450, 250, 0, 360, r);
    }
    settextstyle(8, 0, 3);
    outtextxy(380, 230, "C-Computer");
    int ch = getch();
    if (ch == 70 || ch == 102)
        mode = 1;
    else if (ch == 99 || ch == 67)
        mode = 2;
    return 1;
}

int main()
{
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "C:\\TC\\BGI");
    int ch, chp;

    ch = home();

    while (1)
    {
        if (ch == 84 || ch == 116)
            ch = tutorial();
        if (ch == 72 || ch == 104)
            ch = home();
        if (ch == 80 || ch == 112)
        { choice();
            rules();
            setgame();
            play();
        }
        else if (ch == 81 || ch == 113)
            exit(1);
        else
            exit(1);
    }

    getch();
    closegraph();
    return 0;
}
