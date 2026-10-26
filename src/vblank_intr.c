#include <stdint.h>

typedef uint8_t bool8;
typedef void (*IntrCallback)(void);
typedef void (*MainCallback)(void);

struct MainVBlankState
{
    MainCallback callback1;
    MainCallback callback2;
    uint8_t unknown_008[4];
    IntrCallback vblankCallback;
    IntrCallback hblankCallback;
    IntrCallback vcountCallback;
    IntrCallback serialCallback;
    uint16_t intrCheck;
    uint16_t unknown_01e;
    uint32_t *vblankCounter1;
    uint32_t vblankCounter2;
    
};

struct SoundInfoVBlank
{
    uint8_t unknown_000[4];
    uint8_t pcmDmaCounter;
};

extern struct MainVBlankState gMain;
extern uint8_t gWirelessCommType;
extern uint8_t gLinkVSyncDisabled;
extern uint8_t gPcmDmaCounter;
extern struct SoundInfoVBlank gSoundInfo;
extern uint8_t sVcountBeforeSound;
extern uint8_t sVcountAfterSound;
extern void RfuVSync(void);
extern void LinkVSync(void);
extern void CopyBufferedValuesToGpuRegs(void);
extern void ProcessDma3Requests(void);
extern void m4aSoundMain(void);
extern void TryReceiveLinkBattleData(void);
extern void UpdateWirelessStatusIndicatorSprite(void);
extern uint16_t Random(void);

#define REG_VCOUNT (*(volatile uint16_t *)0x04000006)
#define INTR_CHECK (*(volatile uint16_t *)0x03007FF8)
#define INTR_FLAG_VBLANK 1

void VBlankIntr(void)
{
    if (gWirelessCommType != 0)
        RfuVSync();
    else if (!gLinkVSyncDisabled)
        LinkVSync();
    if (gMain.vblankCounter1 != 0)
        (*gMain.vblankCounter1)++;
    if (gMain.vblankCallback != 0)
        gMain.vblankCallback();
    gMain.vblankCounter2++;
    CopyBufferedValuesToGpuRegs();
    ProcessDma3Requests();
    gPcmDmaCounter = gSoundInfo.pcmDmaCounter;
    sVcountBeforeSound = (uint8_t)REG_VCOUNT;
    m4aSoundMain();
    sVcountAfterSound = (uint8_t)REG_VCOUNT;
    TryReceiveLinkBattleData();
    Random();
    UpdateWirelessStatusIndicatorSprite();
    INTR_CHECK |= INTR_FLAG_VBLANK;
    gMain.intrCheck |= INTR_FLAG_VBLANK;
}
