#include <stdint.h>
typedef uint8_t bool8;typedef void (*IntrCallback)(void);typedef void (*MainCallback)(void);
struct MainVBlankState{MainCallback callback1,callback2;uint8_t unknown_008[4];IntrCallback vblankCallback,hblankCallback,vcountCallback,serialCallback;uint16_t intrCheck;uint16_t unknown_01e;uint32_t *vblankCounter1;uint32_t vblankCounter2;};
struct SoundInfoVBlank{uint8_t unknown_000[4];uint8_t pcmDmaCounter;};
extern struct MainVBlankState gMain;extern uint8_t gWirelessCommType,gLinkVSyncDisabled,gPcmDmaCounter,sVcountBeforeSound,sVcountAfterSound;extern struct SoundInfoVBlank gSoundInfo;
extern void RfuVSync(void),LinkVSync(void),CopyBufferedValuesToGpuRegs(void),ProcessDma3Requests(void),m4aSoundMain(void),TryReceiveLinkBattleData(void),UpdateWirelessStatusIndicatorSprite(void);extern uint16_t Random(void);
#define REG_VCOUNT (*(volatile uint16_t *)0x04000006)
#define INTR_CHECK (*(volatile uint16_t *)0x03007FF8)
#define INTR_FLAG_VBLANK 1
/* BPGJ rev0: 0x08000724..0x080007a7. */
void VBlankIntr(void)
{
 if(gWirelessCommType!=0)RfuVSync();else if(!gLinkVSyncDisabled)LinkVSync();
 if(gMain.vblankCounter1)(*gMain.vblankCounter1)++;
 if(gMain.vblankCallback)gMain.vblankCallback();
 gMain.vblankCounter2++;
 CopyBufferedValuesToGpuRegs();ProcessDma3Requests();
 gPcmDmaCounter=gSoundInfo.pcmDmaCounter;
 sVcountBeforeSound=(uint8_t)REG_VCOUNT;m4aSoundMain();sVcountAfterSound=(uint8_t)REG_VCOUNT;
 TryReceiveLinkBattleData();Random();UpdateWirelessStatusIndicatorSprite();
 INTR_CHECK|=INTR_FLAG_VBLANK;gMain.intrCheck|=INTR_FLAG_VBLANK;
}

