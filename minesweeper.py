# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
import random

load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')# IT SHOULD BE WORKING USING THIS IN THE FUTUTRE
TOKEN = os.getenv('DISCORD_TOKEN')

#GUILD = os.getenv('DISCORD_GUILD')

#client = discord.Client()
bot = commands.Bot(command_prefix = 'm!')
#@client.event
#async def on_ready():
#    for guild in client.guilds:
#        if guild.name == GUILD:
#            break
#
#    print(
#        f'{client.user} is connected to the following guild:\n'
#        f'{guild.name}(id: {guild.id})'
#    )


#client.run(TOKEN)


#minesweeper
@bot.command(name='minesweeper', help='Play a game of minesweeper in one of three difficulties')
async def mines(ctx):
    if ctx.author == bot.user:
        return
    if ctx.message.content == 'm!minesweeper easy':
        bomb_array = [0] * 81
        bomb_array[0:10] = [9]*10
        random.shuffle(bomb_array)
        for b in range(0,len(bomb_array)):
            if bomb_array[b]>=9:
                if ((b-10) >= 0) and (b//9 == ((b-10)//9)+1):
                    bomb_array[b-10]+=1
                if ((b-9) >= 0 ):
                    bomb_array[b-9]+=1 
                if ((b-8) >= 0) and (b//9 == ((b-8)//9)+1):
                    bomb_array[b-8]+=1
                if (((b-1) >= 0) and (b//9 == (b-1)//9)):
                    bomb_array[b-1]+=1
                if (((b+1) <= 80) and (b//9 == (b+1)//9)):
                    bomb_array[b+1]+=1
                if ((b+8) <= 80 )and (b//9 == ((b+8)//9)-1):
                    bomb_array[b+8]+=1
                if ((b+9) <= 80 ):
                    bomb_array[b+9]+=1
                if ((b+10) <= 80 ) and (b//9 == ((b+10)//9)-1):
                    bomb_array[b+10]+=1

        for c in range(0,len(bomb_array)):
            if bomb_array[c] >= 9:
                bomb_array[c] = '||:x:||'
        
        for c in range(0,len(bomb_array)):
            if bomb_array[c] == 0:
                bomb_array[c] = '||:zero:||'
            if bomb_array[c] == 1:
                bomb_array[c] = '||:one:||'
            if bomb_array[c] == 2:
                bomb_array[c] = '||:two:||'
            if bomb_array[c] == 3:
                bomb_array[c] = '||:three:||'
            if bomb_array[c] == 4:
                bomb_array[c] = '||:four:||'
            if bomb_array[c] == 5:
                bomb_array[c] = '||:five:||'
            if bomb_array[c] == 6:
                bomb_array[c] = '||:six:||'
            if bomb_array[c] == 7:
                bomb_array[c] = '||:seven:||'
            if bomb_array[c] == 8:
                bomb_array[c] = '||:eight:||'
        
        r1 = bomb_array[0:9]
        r2 = bomb_array[9:18]
        r3 = bomb_array[18:27]
        r4 = bomb_array[27:36]
        r5 = bomb_array[36:45]
        r6 = bomb_array[45:54]
        r7 = bomb_array[54:63]
        r8 = bomb_array[63:72]
        r9 = bomb_array[72:81]                

        for i in range(1,9):
            r1[0]+=r1[1]
            del r1[1]
            r2[0]+=r2[1]
            del r2[1]
            r3[0]+=r3[1]
            del r3[1]
            r4[0]+=r4[1]
            del r4[1]
            r5[0]+=r5[1]
            del r5[1]
            r6[0]+=r6[1]
            del r6[1]
            r7[0]+=r7[1]
            del r7[1]
            r8[0]+=r8[1]
            del r8[1]
            r9[0]+=r9[1]
            del r9[1]

        r1=str(r1)
        r1 = r1[2:-2]
        r2=str(r2)
        r2 = r2[2:-2]
        r3=str(r3)
        r3 = r3[2:-2]
        r4=str(r4)
        r4 = r4[2:-2]
        r5=str(r5)
        r5 = r5[2:-2]
        r6=str(r6)
        r6 = r6[2:-2]
        r7=str(r7)
        r7 = r7[2:-2]
        r8=str(r8)
        r8 = r8[2:-2]
        r9=str(r9)
        r9 = r9[2:-2]

        await ctx.send(r1+'\n'+r2+'\n'+r3+'\n'+r4+'\n'+r5+'\n'+r6+'\n'+r7+'\n'+r8+'\n'+r9)

    if ctx.message.content == 'm!minesweeper intermediate':
        bomb_array = [0] * 256
        bomb_array[0:40] = [9]*40
        random.shuffle(bomb_array)
        for b in range(0,len(bomb_array)):
            if bomb_array[b]>=9:
                if ((b-17) >= 0) and (b//16 == ((b-17)//16)+1):
                    bomb_array[b-17]+=1
                if ((b-16) >= 0 ):
                    bomb_array[b-16]+=1 
                if ((b-15) >= 0) and (b//16 == ((b-15)//16)+1):
                    bomb_array[b-15]+=1
                if (((b-1) >= 0) and (b//16 == (b-1)//16)):
                    bomb_array[b-1]+=1
                if (((b+1) <= 255) and (b//16 == (b+1)//16)):
                    bomb_array[b+1]+=1
                if ((b+15) <= 255 )and (b//16 == ((b+15)//16)-1):
                    bomb_array[b+15]+=1
                if ((b+16) <= 255 ):
                    bomb_array[b+16]+=1
                if ((b+17) <= 255 ) and (b//16 == ((b+17)//16)-1):
                    bomb_array[b+17]+=1

        for c in range(0,len(bomb_array)):
            if bomb_array[c] >= 9:
                bomb_array[c] = '||:x:||'
                
        for c in range(0,len(bomb_array)):
            if bomb_array[c] == 0:
                bomb_array[c] = '||:zero:||'
            if bomb_array[c] == 1:
                bomb_array[c] = '||:one:||'
            if bomb_array[c] == 2:
                bomb_array[c] = '||:two:||'
            if bomb_array[c] == 3:
                bomb_array[c] = '||:three:||'
            if bomb_array[c] == 4:
                bomb_array[c] = '||:four:||'
            if bomb_array[c] == 5:
                bomb_array[c] = '||:five:||'
            if bomb_array[c] == 6:
                bomb_array[c] = '||:six:||'
            if bomb_array[c] == 7:
                bomb_array[c] = '||:seven:||'
            if bomb_array[c] == 8:
                bomb_array[c] = '||:eight:||'
                
        r1 = bomb_array[0:16]
        r2 = bomb_array[16:32]
        r3 = bomb_array[32:48]
        r4 = bomb_array[48:64]
        r5 = bomb_array[64:80]
        r6 = bomb_array[80:96]
        r7 = bomb_array[96:112]
        r8 = bomb_array[112:128]
        r9 = bomb_array[128:144]
        r10 = bomb_array[144:160]
        r11 = bomb_array[160:176]
        r12 = bomb_array[176:192]
        r13 = bomb_array[192:208]
        r14 = bomb_array[208:224]
        r15 = bomb_array[224:240]
        r16 = bomb_array[240:256]
           
                

        for i in range(1,16):
            r1[0]+=r1[1]
            del r1[1]
            r2[0]+=r2[1]
            del r2[1]
            r3[0]+=r3[1]
            del r3[1]
            r4[0]+=r4[1]
            del r4[1]
            r5[0]+=r5[1]
            del r5[1]
            r6[0]+=r6[1]
            del r6[1]
            r7[0]+=r7[1]
            del r7[1]
            r8[0]+=r8[1]
            del r8[1]
            r9[0]+=r9[1]
            del r9[1]
            r10[0]+=r10[1]
            del r10[1]
            r11[0]+=r11[1]
            del r11[1]
            r12[0]+=r12[1]
            del r12[1]
            r13[0]+=r13[1]
            del r13[1]
            r14[0]+=r14[1]
            del r14[1]
            r15[0]+=r15[1]
            del r15[1]
            r16[0]+=r16[1]
            del r16[1]

        r1=str(r1)
        r1 = r1[2:-2]
        r2=str(r2)
        r2 = r2[2:-2]
        r3=str(r3)
        r3 = r3[2:-2]
        r4=str(r4)
        r4 = r4[2:-2]
        r5=str(r5)
        r5 = r5[2:-2]
        r6=str(r6)
        r6 = r6[2:-2]
        r7=str(r7)
        r7 = r7[2:-2]
        r8=str(r8)
        r8 = r8[2:-2]
        r9=str(r9)
        r9 = r9[2:-2]
        r10=str(r10)
        r10 = r10[2:-2]
        r11=str(r11)
        r11 = r11[2:-2]
        r12=str(r12)
        r12 = r12[2:-2]
        r13=str(r13)
        r13 = r13[2:-2]
        r14=str(r14)
        r14 = r14[2:-2]
        r15=str(r15)
        r15 = r15[2:-2]
        r16=str(r16)
        r16 = r16[2:-2]
        #await ctx.send(r1+'\n'+r2+'\n'+r3+'\n'+r4+'\n'+r5+'\n'+r6+'\n'+r7+'\n'+r8+'\n')
        #await ctx.send(r9+'\n'+r10+'\n'+r11+'\n'+r12+'\n'+r13+'\n'+r14+'\n'+r15+'\n'+r16)
        await ctx.send(r1+'\n'+r2+'\n'+r3+'\n'+r4+'\n'+r5+'\n'+r6+'\n')
        await ctx.send(r7+'\n'+r8+'\n'+r9+'\n'+r10+'\n'+r11+'\n'+r12+'\n')
        await ctx.send(r13+'\n'+r14+'\n'+r15+'\n'+r16)

    if ctx.message.content == 'm!minesweeper expert':
        bomb_array = [0] * 480
        bomb_array[0:99] = [9]*99
        random.shuffle(bomb_array)
        for b in range(0,len(bomb_array)):
            if bomb_array[b]>=9:
                if ((b-31) >= 0) and (b//30 == ((b-31)//30)+1):
                    bomb_array[b-31]+=1
                if ((b-30) >= 0 ):
                    bomb_array[b-30]+=1 
                if ((b-29) >= 0) and (b//30 == ((b-29)//30)+1):
                    bomb_array[b-29]+=1
                if (((b-1) >= 0) and (b//30 == (b-1)//30)):
                    bomb_array[b-1]+=1
                if (((b+1) <= 479) and (b//30 == (b-1)//30)):
                    bomb_array[b+1]+=1
                if ((b+29) <= 479 )and (b//30 == ((b+29)//30)-1):
                    bomb_array[b+29]+=1
                if ((b+30) <= 479 ):
                    bomb_array[b+30]+=1
                if ((b+31) <= 479 ) and (b//30 == ((b+31)//30)-1):
                    bomb_array[b+31]+=1

        for c in range(0,len(bomb_array)):
            if bomb_array[c] >= 9:
                bomb_array[c] = '||:x:||'
        
        for c in range(0,len(bomb_array)):
            if bomb_array[c] == 0:
                bomb_array[c] = '||:zero:||'
            if bomb_array[c] == 1:
                bomb_array[c] = '||:one:||'
            if bomb_array[c] == 2:
                bomb_array[c] = '||:two:||'
            if bomb_array[c] == 3:
                bomb_array[c] = '||:three:||'
            if bomb_array[c] == 4:
                bomb_array[c] = '||:four:||'
            if bomb_array[c] == 5:
                bomb_array[c] = '||:five:||'
            if bomb_array[c] == 6:
                bomb_array[c] = '||:six:||'
            if bomb_array[c] == 7:
                bomb_array[c] = '||:seven:||'
            if bomb_array[c] == 8:
                bomb_array[c] = '||:eight:||'
        
        r1 = bomb_array[0:30]
        r2 = bomb_array[30:60]
        r3 = bomb_array[60:90]
        r4 = bomb_array[90:120]
        r5 = bomb_array[120:150]
        r6 = bomb_array[150:180]
        r7 = bomb_array[180:210]
        r8 = bomb_array[210:240]
        r9 = bomb_array[240:270]
        r10 = bomb_array[270:300]
        r11 = bomb_array[300:330]
        r12 = bomb_array[330:360]
        r13 = bomb_array[360:390]
        r14 = bomb_array[390:420]
        r15 = bomb_array[420:450]
        r16 = bomb_array[450:480]

        for i in range(1,30):
            r1[0]+=r1[1]
            del r1[1]
            r2[0]+=r2[1]
            del r2[1]
            r3[0]+=r3[1]
            del r3[1]
            r4[0]+=r4[1]
            del r4[1]
            r5[0]+=r5[1]
            del r5[1]
            r6[0]+=r6[1]
            del r6[1]
            r7[0]+=r7[1]
            del r7[1]
            r8[0]+=r8[1]
            del r8[1]
            r9[0]+=r9[1]
            del r9[1]
            r10[0]+=r10[1]
            del r10[1]
            r11[0]+=r11[1]
            del r11[1]
            r12[0]+=r12[1]
            del r12[1]
            r13[0]+=r13[1]
            del r13[1]
            r14[0]+=r14[1]
            del r14[1]
            r15[0]+=r15[1]
            del r15[1]
            r16[0]+=r16[1]
            del r16[1]

        r1=str(r1)
        r1 = r1[2:-2]
        r2=str(r2)
        r2 = r2[2:-2]
        r3=str(r3)
        r3 = r3[2:-2]
        r4=str(r4)
        r4 = r4[2:-2]
        r5=str(r5)
        r5 = r5[2:-2]
        r6=str(r6)
        r6 = r6[2:-2]
        r7=str(r7)
        r7 = r7[2:-2]
        r8=str(r8)
        r8 = r8[2:-2]
        r9=str(r9)
        r9 = r9[2:-2]
        r10=str(r10)
        r10 = r10[2:-2]
        r11=str(r11)
        r11 = r11[2:-2]
        r12=str(r12)
        r12 = r12[2:-2]
        r13=str(r13)
        r13 = r13[2:-2]
        r14=str(r14)
        r14 = r14[2:-2]
        r15=str(r15)
        r15 = r15[2:-2]
        r16=str(r16)
        r16 = r16[2:-2]

        await ctx.send(r1+'\n'+r2+'\n'+r3+'\n'+r4+'\n')
        await ctx.send(r5+'\n'+r6+'\n'+r7+'\n'+r8+'\n')
        await ctx.send(r9+'\n'+r10+'\n'+r11+'\n'+r12+'\n')
        await ctx.send(r13+'\n'+r14+'\n'+r15+'\n'+r16)


bot.run(TOKEN)
