
#Цей код імпортує необхідні модулі для використання Pygame. 
import pygame, random, sys 
from pygame.locals import * 
#Ці змінні визначають різні параметри гри, такі як розміри вікна (WINDOWWIDTH і WINDOWHEIGHT), кольори (TEXTCOLOR і BACKGROUNDCOLOR), частота кадрів на секунду (FPS), розміри та швидкість ворогів (BADDIEMINSIZE, BADDIEMAXSIZE, BADDIEMINSPEED, BADDIEMAXSPEED), частота додавання нових ворогів (ADDNEWBADDIERATE), швидкість руху гравця (PLAYERMOVERATE) та розмір поаданів (PAODANSIZE). 
 
WINDOWWIDTH = 600 
WINDOWHEIGHT = 600 
TEXTCOLOR = (0, 0, 0) 
BACKGROUNDCOLOR = (255, 255, 255) 
FPS = 60 
BADDIEMINSIZE = 30 
BADDIEMAXSIZE = 60 
BADDIEMINSPEED = 1 
BADDIEMAXSPEED = 7 
ADDNEWBADDIERATE = 20 
PLAYERMOVERATE = 5 
PAODANSIZE=10 
 
#Ця функція використовується для завершення гри та виходу з програми 
 
def terminate(): 
    pygame.quit() 
    sys.exit() 
 
#Ця функція очікує, доки гравець натисне клавішу, перед тим як почати гру. Вона перевіряє події, які виникають, і якщо гравець натиснув клавішу, то функція повертається. 
def waitForPlayerToPressKey(): 
    while True: 
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                terminate() 
            if event.type == KEYDOWN: 
                if event.key == K_ESCAPE:  
                    terminate() 
                return 
 
#Ця функція перевіряє, чи гравець зіткнувся з ворогом. Вона перевіряє перетин прямокутників гравця (playerRect) і ворога (baddies). Якщо перетин відбувається, функція повертає True, що означає зіткнення. 
 
def playerHasHitBaddie(playerRect, baddies): 
    for b in baddies: 
        if playerRect.colliderect(b['rect']): 
            return True 
    return False 
 
#Ця функція перевіряє, чи поадани гравця (paodans) зіткнулися з ворогами (baddies). Вона перевіряє перетин прямокутників поаданів і ворогів. Якщо відбувається перетин, то відповідно до розміру ворога (менш або більше за середнє значення розмірів ворогів), до змінної score додається 5 або 10 балів. Поадання та вороги, які зіткнулися, видаляються з відповідних списків. 
 
def paodanHasHitBaddie(paodans, baddies,score): 
    for paodan in paodans[:]: 
        for b in baddies[:]: 
            if paodan['rect'].colliderect(b['rect']): 
                if b['rect'].width < (BADDIEMAXSIZE+BADDIEMINSIZE)/2 : 
                    score += 5 
                else: 
                    score += 10 
                paodans.remove(paodan) 
                baddies.remove(b) 
 
    return score 
 
#Ця функція відповідає за відображення тексту на поверхні. Вона створює текстовий об'єкт з заданим текстом, шрифтом та кольором, встановлює його положення і накладає його на поверхню. 
 
def drawText(text, font, surface, x, y): 
    textobj = font.render(text, 0, TEXTCOLOR) 
    textrect = textobj.get_rect() 
    textrect.topleft = (int(x), int(y)) 
    surface.blit(textobj, textrect) 
 
 
 
#Цей код ініціалізує Pygame, створює вікно гри з встановленими розмірами (WINDOWWIDTH і WINDOWHEIGHT), встановлює заголовок вікна на "Dodger" та приховує курсор миші. 
 
pygame.init() 
mainClock = pygame.time.Clock() 
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT)) 
pygame.display.set_caption('Dodger') 
pygame.mouse.set_visible(False) 
 
#Цей код визначає шрифт для відображення тексту за замовчуванням. 
 
font = pygame.font.SysFont(None, 48) 
 
 
 
#Цей код завантажує зображення гравця, ворогів та поадан 
 
playerImage = pygame.image.load('player.png') 
playerRect = playerImage.get_rect() 
baddieImage = pygame.image.load('baddie.png') 
paodanImage =pygame.image.load('enemy.png') 
 
#Ця функція відправляє поадані (проектил) від гравця. Вона створює новий поадан з прямокутною областю (rect), швидкістю руху (speed) та зображенням (surface), яке масштабується до розміру PAODANSIZE. Потім цей новий поадан додається до списку поаданів (paodans). 
 
def send_paodan(x,y,paodans): 
    newPaodan = { 
        'rect': pygame.Rect(x,y,PAODANSIZE, PAODANSIZE), 
        'speed': 10, 
        'surface': pygame.transform.scale(paodanImage, (PAODANSIZE,

PAODANSIZE))

ZE)), 
        } 
    paodans.append(newPaodan) 
 
#Цей код очищує поверхню вікна і відображає початковий текст гри "Dodger" та інструкцію "Press a key to start.". Потім викликається функція pygame.display.update(), щоб оновити вміст вікна. Після цього очікується, доки гравець натисне клавішу для початку гри. 
 
windowSurface.fill(BACKGROUNDCOLOR) 
drawText('Dodger', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3)) 
drawText('Press a key to start.', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50) 
pygame.display.update() 
waitForPlayerToPressKey() 
 
#Цей код встановлює початкові значення змінних для нової гри. Змінна topScore визначає найкращий результат гравця. Змінні baddies і paodans є списками для зберігання ворогів і поаданів відповідно. Змінна score містить поточний результат гравця. Змінні moveLeft, moveRight, moveUp, moveDown визначають напрямок руху гравця. Змінні reverseCheat і slowCheat використовуються для активації шахрайських режимів гри. Змінна baddieAddCounter визначає лічильник для додавання нових ворогів. 
 
topScore = 0 
while True: 
     
    baddies = [] 
    paodans = [] 
    score = 0 
    playerRect.topleft = (WINDOWWIDTH // 2, WINDOWHEIGHT - 50) 
    moveLeft = moveRight = moveUp = moveDown = False 
    reverseCheat = slowCheat = False 
    baddieAddCounter = 0 
 
#Цей код обробляє всі події pygame, які відбуваються в грі. Він перевіряє тип кожної події і виконує відповідні дії. Наприклад, якщо подія є натисканням клавіші, він встановлює відповідні змінні руху гравця (moveLeft, moveRight, moveUp, moveDown) або відправляє поадан від гравця, якщо натиснута клавіша пробілу. Якщо подія є звільненням клавіші, він скидає відповідні змінні руху гравця. Якщо подія є переміщенням миші, він оновлює координати гравця відповідно до позиції миші. 
 
    while True:  
 
 
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                terminate() 
 
            if event.type == KEYDOWN: 
                if event.key == K_z: 
                    reverseCheat = True 
                if event.key == K_x: 
                    slowCheat = True 
                if event.key == K_LEFT or event.key == K_a: 
                    moveRight = False 
                    moveLeft = True 
                if event.key == K_RIGHT or event.key == K_d: 
                    moveLeft = False 
                    moveRight = True 
                if event.key == K_UP or event.key == K_w: 
                    moveDown = False 
                    moveUp = True 
                if event.key == K_DOWN or event.key == K_s: 
                    moveUp = False 
                    moveDown = True 
                if event.key ==K_SPACE: 
                    send_paodan(playerRect.centerx,playerRect.centery,paodans) 
 
            if event.type == KEYUP: 
                if event.key == K_z: 
                    reverseCheat = False 
                    #score = 0 
                if event.key == K_x: 
                    slowCheat = False 
                    #score = 0 
                if event.key == K_ESCAPE: 
                        terminate() 
 
                if event.key == K_LEFT or event.key == K_a: 
                    moveLeft = False 
                if event.key == K_RIGHT or event.key == K_d: 
                    moveRight = False 
                if event.key == K_UP or event.key == K_w: 
                    moveUp = False 
                if event.key == K_DOWN or event.key == K_s: 
                    moveDown = False 
 
            if event.type == MOUSEMOTION: 
                playerRect.centerx = event.pos[0] 
                playerRect.centery = event.pos[1] 
        
       #Цей код відповідає за додавання нових ворогів в гру. Він перевіряє, чи не активовані шахрайські режими гри (reverseCheat і slowCheat), і якщо ні, то збільшує лічильник baddieAddCounter. Якщо лічильник досягає значення ADDNEWBADDIERATE, він скидає лічильник на 0 і створює нового ворога з випадковими параметрами, такими як розмір, швидкість і зображення. Потім новий ворог додається

до списку baddies. 
 
        if not reverseCheat and not slowCheat: 
            baddieAddCounter += 1 
        if baddieAddCounter == ADDNEWBADDIERATE: 
            baddieAddCounter = 0 
            baddieSize = random.randint(BADDIEMINSIZE, BADDIEMAXSIZE) 
            newBaddie = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - baddieSize), 0 - baddieSize, baddieSize, baddieSize), 
                        'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED), 
                        'surface':pygame.transform.scale(baddieImage, (baddieSize, baddieSize)), 
                        } 
 
            baddies.append(newBaddie) 
 
        #Цей код відповідає за переміщення гравця відповідно до значень змінних руху (moveLeft, moveRight, moveUp, moveDown). Якщо значення moveLeft встановлено на True і ліва сторона прямокутника гравця ще не досягла лівого краю вікна, то гравець зміщується вліво на відстань PLAYERMOVERATE. Аналогічно для руху вправо, вгору і вниз. 
 
        if moveLeft and playerRect.left > 0: 
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0) 
        if moveRight and playerRect.right < WINDOWWIDTH: 
            playerRect.move_ip(PLAYERMOVERATE, 0) 
        if moveUp and playerRect.top > 0: 
            playerRect.move_ip(0, -1 * PLAYERMOVERATE) 
        if moveDown and playerRect.bottom < WINDOWHEIGHT: 
            playerRect.move_ip(0, PLAYERMOVERATE) 
 
 
 
        #Цей код відповідає за рух ворогів вниз. Якщо не активовані шахрайські режими (reverseCheat і slowCheat), то кожен ворог рухається вниз зі своєю власною швидкістю. Якщо активовано режим reverseCheat, то вороги рухаються вгору зі швидкістю -5. Якщо активовано режим slowCheat, то вороги рухаються вниз зі швидкістю 1. 
 
        for b in baddies: 
            if not reverseCheat and not slowCheat: 
                b['rect'].move_ip(0, b['speed']) 
            elif reverseCheat: 
                b['rect'].move_ip(0, -5) 
            elif slowCheat: 
                b['rect'].move_ip(0, 1) 
 
        #Цей код відповідає за видалення ворогів, які вийшли за межі вікна гри. Він перебирає всіх ворогів у списку baddies і перевіряє, чи вони знаходяться нижче нижньої межі вікна (WINDOWHEIGHT). Якщо так, то ворог видаляється зі списку baddies. 
 
        for b in baddies[:]: 
            if b['rect'].top > WINDOWHEIGHT: 
                baddies.remove(b) 
         
        #Цей код відповідає за рух поаданів (снарядів) вгору та видалення поаданів, які вийшли за верхню межу вікна. Перший цикл переміщує кожен поадан вгору з його власною швидкістю. Другий цикл перебирає всі поадани в списку paodans і перевіряє, чи їх нижня сторона знаходиться вище або на межі 4 пікселів від верхньої межі вікна. Якщо так, то поадан видаляється зі списку paodans. 
 
        for paodan in paodans: 
            if not reverseCheat and not slowCheat: 
                paodan['rect'].move_ip(0, -paodan['speed']) 
        for paodan in paodans[:]: 
            if paodan['rect'].bottom <=4: 
                paodans.remove(paodan) 
         
        #Решта коду відповідає за відображення елементів гри, оновлення екрану, перевірку зіткнення гравця з ворогами та обробку кінця гри. 
 
        score = paodanHasHitBaddie(paodans, baddies, score) 
 
 
        
        windowSurface.fill(BACKGROUNDCOLOR) 
 
         
        drawText('Score: %s' % (score), font, windowSurface, 10, 0) 
        drawText('Top Score: %s' % (topScore), font, windowSurface, 10, 40) 
 
         
        windowSurface.blit(playerImage, playerRect) 
 
         
        for b in baddies: 
            windowSurface.blit(b['surface'], b['rect']) 
 
        for paodan in paodans: 
            windowSurface.blit(paodan['surface'], paodan['rect']) 
 
        pygame.display.update() 
 
         
        if playerHasHitBaddie(playerRect, baddies): 
            if score > topScore: 
                topScore = score  
            break 
 
        mainClock.tick(FPS) 
 
    
 
    #Цей рядок коду відповідає за відображення надпису "GAME OVER" на екрані гри. Використовується функція drawText, яка отримує текст, шрифт,

поверхню для малювання та координати для розміщення тексту. 
    drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3)) 
     
    #Цей рядок коду відповідає за відображення надпису "Press a key to play again." на екрані гри. Використовується та ж функція drawText, але з іншим текстом та іншими координатами для розміщення. 
    drawText('Press a key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50) 
     
    #Цей рядок коду оновлює вміст екрану, щоб відобразити нові надписи "GAME OVER" і "Press a key to play again". 
    pygame.display.update() 
     
    #Цей рядок коду очікує, доки гравець натисне будь-яку клавішу, перш ніж продовжити гру. Використовується функція waitForPlayerToPressKey, яка блокує виконання програми, поки не виникне подія натискання клавіші. Після натискання клавіші гра буде починатися знову. 
    waitForPlayerToPressKey()