#include <stdint.h>

typedef void (*IntrFunc)(void);

/* sTimerIntrFunc aliases gIntrTable + 7. */
extern IntrFunc *const sTimerIntrFunc;
extern void SetFlashTimerIntr(uint8_t timer, IntrFunc *handlerSlot);

void InitFlashTimer(void)
{
    IntrFunc **func = (IntrFunc **)&sTimerIntrFunc;
    SetFlashTimerIntr(2, *func);
}

