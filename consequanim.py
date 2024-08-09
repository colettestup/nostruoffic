multiprocessing.Process(target=LED_control, name="LED", args=(duration, LED_STATE_FLASHING)).start()
