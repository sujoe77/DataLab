a send operation will block if:
	the buffer is full -> continue when something removed from buffer and there is empty space
	if the buffer is zero size (no buffer), and there is no waiting receiver -> when receiver pick up the item

works like java blocking queue?

