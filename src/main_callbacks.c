#include <stddef.h>
#include <stdint.h>
typedef uint8_t bool8; typedef void (*MainCallback)(void);
struct MainState { MainCallback callback1; MainCallback callback2; uint8_t unknown_008[0x430]; uint8_t state; };
extern struct MainState gMain; extern void CopyrightScreenInit(void); extern bool8 HandleLinkConnection(void); extern bool8 RunSaveFailedScreen(void); extern bool8 RunHelpSystemCallback(void);
extern void *gSaveBlock1Ptr,*gSaveBlock2Ptr; extern uint8_t gSaveBlock1[],gSaveBlock2[]; extern uint32_t gSaveBlock2EncryptionKey; extern uint8_t gQuestLogPlaybackState;
void CallCallbacks(void); void SetMainCallback2(MainCallback);
/* BPGJ rev0: 0x080004b0..0x080004c3 */
void UpdateLinkAndCallCallbacks(void){if(!HandleLinkConnection())CallCallbacks();}
/* BPGJ rev0: 0x080004c4..0x080004f3 */
void InitMainCallbacks(void){*(uint32_t *)((uint8_t *)&gMain+0x20)=0;*(uint32_t *)((uint8_t *)&gMain+0x24)=0;gMain.callback1=NULL;SetMainCallback2(CopyrightScreenInit);gSaveBlock2Ptr=gSaveBlock2;gSaveBlock1Ptr=gSaveBlock1;gSaveBlock2EncryptionKey=0;gQuestLogPlaybackState=0;}
/* BPGJ rev0: 0x08000510..0x0800053f */
void CallCallbacks(void){if(!RunSaveFailedScreen()&&!RunHelpSystemCallback()){if(gMain.callback1)gMain.callback1();if(gMain.callback2)gMain.callback2();}}
/* BPGJ rev0: 0x08000544..0x08000553 */
void SetMainCallback2(MainCallback callback){gMain.callback2=callback;gMain.state=0;}
