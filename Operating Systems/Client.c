
#include<sys/msg.h>
#include<unistd.h>
#include<string.h>
#include<stdio.h>
#include<stdlib.h>
struct mymsg
{ long mtype;
  char mtext[10];}msg1,msg2;
int main()
{ int msgid,l1=10,l2=10,id;
  pid_t pid;
  msgid=msgget(123,IPC_CREAT|0666);
  printf("\nMessage queue id %d",msgid);
  msg1.mtype=msg2.mtype=1;
  pid=fork();
  if(msgid<0||pid<0)
  { printf("\nIts an error");
    exit(0);}
  else
  { if(pid>0)
    { printf("\nEnter the message: ");
      scanf("%s",msg1.mtext);
      l1=strlen(msg1.mtext);
      msgsnd(msgid,&msg1,l1,0);
      printf("\nThe message by parent sent to child: ");