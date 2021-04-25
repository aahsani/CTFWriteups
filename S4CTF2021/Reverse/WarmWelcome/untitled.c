
undefined8 main(void)

{
  int iVar1;
  time_t tVar2;
  char local_93 [2]; //0
  char local_91 [2]; //4
  char local_8f; //T
  undefined local_8e; //h
  undefined local_8d; //3
  undefined local_8c; //_
  undefined local_8b; //F
  undefined local_8a; //i
  char local_88; //S
  char local_87; //4
  char local_86; //C
  char local_85; //T 
  char local_84; //F
  char local_83; //{
  char local_82; //A
  char local_81; //_
  char local_80; //v
  int local_7f; //3ry_
  int local_7b; //Warm
  char local_77; //_
  char acStack118 [18]; //We1c0m3_fr0m_S4LAB
  int local_64; //_enj
  char local_60; //0 ??
  char local_5f; //y
  char local_5e; //_
  char acStack93 [6]; //Th3_F1
  char local_57; //4 
  char local_56; //g
  char local_55; //}
  timespec local_48;
  void *local_30;
  void *local_28;
  void *local_20;
  void *local_18;
  size_t local_10;
  
  local_48.tv_sec = 0;
  local_48.tv_nsec = 25000000;
  local_10 = 200;
  ncurses_init();
  tVar2 = time((time_t *)0x0);
  srand((uint)tVar2);
  local_18 = calloc(0x20,local_10);
  local_20 = calloc(0x20,local_10);
  local_28 = calloc(0x20,local_10);
  local_30 = calloc(0x20,local_10);
  particle_init(local_18,local_10,local_10);
  particle_init(local_20,local_10,local_10);
  particle_init(local_28,local_10,local_10);
  particle_init(local_30,local_10,local_10);
  while (iVar1 = wgetch(stdscr), iVar1 != 0x71) {
    if ((1.20999992 <= *(float *)((long)local_18 + 0x18)) ||
       (*(float *)((long)local_18 + 0x18) <= 1.18999994)) {
      if ((0.80999994 <= *(float *)((long)local_18 + 0x18)) ||
         (*(float *)((long)local_18 + 0x18) <= 0.78999996)) {
        if ((0.41000000 <= *(float *)((long)local_18 + 0x18)) ||
           (*(float *)((long)local_18 + 0x18) <= 0.38999999)) {
          if (*(float *)((long)local_18 + 0x18) < 0.01000000) {
            particle_init(local_18,local_10,local_10);
          }
        }
        else {
          particle_init(local_30,local_10,local_10);
        }
      }
      else {
        particle_init(local_28,local_10,local_10);
      }
    }
    else {
      particle_init(local_20,local_10,local_10);
    }
    werase(stdscr);
    particle_update(0x3c23d70a,local_18,local_10,local_10);
    particle_update(0x3c23d70a,local_20,local_10,local_10);
    particle_update(0x3c23d70a,local_28,local_10,local_10);
    particle_update(0x3c23d70a,local_30,local_10,local_10);
    particle_draw(local_18,local_10,local_10);
    particle_draw(local_20,local_10,local_10);
    particle_draw(local_28,local_10,local_10);
    particle_draw(local_30,local_10,local_10);
    wrefresh(stdscr);
    nanosleep(&local_48,(timespec *)0x0);
  }
  free(local_18);
  local_18 = (void *)0x0;
  free(local_20);
  local_20 = (void *)0x0;
  free(local_28);
  local_28 = (void *)0x0;
  free(local_30);
  local_30 = (void *)0x0;
  endwin();
  puts("Hope you enjoy the firework we prepared for you! Now give me a flag :))\n");
  read(0,&local_88,0x34);
  sprintf(local_91,"%d",4);
  sprintf(local_93,"%d",0);
  local_8f = 'T';
  local_8e = 0x68;
  local_8d = 0x33;
  local_8c = 0x5f;
  local_8b = 0x46;
  local_8a = 0x31;
  if ((((((((local_88 == 'S') && (local_87 == '4')) && (local_86 == 'C')) &&
         ((local_85 == 'T' && (local_84 == 'F')))) && (local_83 == '{')) &&
       (((local_55 == '}' && (iVar1 = strncmp(acStack118,"We1c0m3_fr0m_S4LAB",0x12), iVar1 == 0)) &&
        ((local_82 == 'A' && (((local_81 == '_' && (local_80 == 'v')) && (local_7b == 0x6d726157))))
        )))) && ((iVar1 = strncmp(acStack93,&local_8f,6), iVar1 == 0 && (local_64 == 0x6a6e655f))))
     && ((local_7f == 0x5f797233 &&
         (((local_77 == local_5e && (local_77 == '_')) &&
          ((local_56 == 'g' &&
           (((local_5f == 'y' && (local_57 == local_91[0])) && (local_60 == local_93[0])))))))))) {
    puts("\rOh Wow you are ready for fun!! :)\n");
    return 0;
  }
  puts("Try harder to have fun!!\n");
  return 0;
}





// S4CTF{A_v3ry_Warm_We1c0m3_fr0m_S4LAB_enj0y_Th3_F14g}
