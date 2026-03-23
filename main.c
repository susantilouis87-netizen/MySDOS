/* kernel.c - MySDOS Mobile 64-bit */

// Alamat UART untuk ARM64 (Standar QEMU Virt)
// Di HP asli, alamat ini bisa berbeda tergantung chipset Snapdragon/Dimensity
#define UART0_DR *((volatile unsigned int*)0x09000000)

void uart_putc(char c) {
    UART0_DR = c;
}

void print(char *s) {
    while (*s) {
        uart_putc(*s++);
    }
}

void main() {
    print("------------------------------------\n");
    print(" MySDOS Mobile 64-Bit is Booting... \n");
    print(" Developed by Louis - Dumai         \n");
    print("------------------------------------\n");
    
    // OS tetap menyala di sini
    while (1);
}
