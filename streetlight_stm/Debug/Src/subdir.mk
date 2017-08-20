################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Src/LoRaMac.c \
../Src/LoRaMacCrypto.c \
../Src/actuated.pb.c \
../Src/adc-board.c \
../Src/adc.c \
../Src/aes.c \
../Src/board.c \
../Src/cmac.c \
../Src/delay.c \
../Src/eeprom-board.c \
../Src/eeprom.c \
../Src/fifo.c \
../Src/gpio-board.c \
../Src/gpio.c \
../Src/gps.c \
../Src/i2c-board.c \
../Src/i2c.c \
../Src/main.c \
../Src/pb_common.c \
../Src/pb_decode.c \
../Src/pb_encode.c \
../Src/rtc-board.c \
../Src/sensed.pb.c \
../Src/spi-board.c \
../Src/sx1272-board.c \
../Src/sx1272.c \
../Src/sysIrqHandlers.c \
../Src/system_stm32l1xx.c \
../Src/timer.c \
../Src/uart-board.c \
../Src/uart.c \
../Src/utilities.c 

OBJS += \
./Src/LoRaMac.o \
./Src/LoRaMacCrypto.o \
./Src/actuated.pb.o \
./Src/adc-board.o \
./Src/adc.o \
./Src/aes.o \
./Src/board.o \
./Src/cmac.o \
./Src/delay.o \
./Src/eeprom-board.o \
./Src/eeprom.o \
./Src/fifo.o \
./Src/gpio-board.o \
./Src/gpio.o \
./Src/gps.o \
./Src/i2c-board.o \
./Src/i2c.o \
./Src/main.o \
./Src/pb_common.o \
./Src/pb_decode.o \
./Src/pb_encode.o \
./Src/rtc-board.o \
./Src/sensed.pb.o \
./Src/spi-board.o \
./Src/sx1272-board.o \
./Src/sx1272.o \
./Src/sysIrqHandlers.o \
./Src/system_stm32l1xx.o \
./Src/timer.o \
./Src/uart-board.o \
./Src/uart.o \
./Src/utilities.o 

C_DEPS += \
./Src/LoRaMac.d \
./Src/LoRaMacCrypto.d \
./Src/actuated.pb.d \
./Src/adc-board.d \
./Src/adc.d \
./Src/aes.d \
./Src/board.d \
./Src/cmac.d \
./Src/delay.d \
./Src/eeprom-board.d \
./Src/eeprom.d \
./Src/fifo.d \
./Src/gpio-board.d \
./Src/gpio.d \
./Src/gps.d \
./Src/i2c-board.d \
./Src/i2c.d \
./Src/main.d \
./Src/pb_common.d \
./Src/pb_decode.d \
./Src/pb_encode.d \
./Src/rtc-board.d \
./Src/sensed.pb.d \
./Src/spi-board.d \
./Src/sx1272-board.d \
./Src/sx1272.d \
./Src/sysIrqHandlers.d \
./Src/system_stm32l1xx.d \
./Src/timer.d \
./Src/uart-board.d \
./Src/uart.d \
./Src/utilities.d 


# Each subdirectory must supply rules for building sources it contributes
Src/%.o: ../Src/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU GCC Compiler'
	@echo $(PWD)
	arm-none-eabi-gcc -mcpu=cortex-m3 -mthumb -mfloat-abi=soft -std=c99 '-D__weak=__attribute__((weak))' -DOVER_THE_AIR_ACTIVATION -DUSE_DEBUGGER -DUSE_BAND_868 '-D__packed="__attribute__((__packed__))"' -DUSE_HAL_DRIVER -DSTM32L151xB -I"/home/thepro/Documents/gitrepos/streetlight/streetlight_stm/Inc" -I"/home/thepro/Documents/gitrepos/streetlight/streetlight_stm/Drivers/STM32L1xx_HAL_Driver/Inc" -I"/home/thepro/Documents/gitrepos/streetlight/streetlight_stm/Drivers/STM32L1xx_HAL_Driver/Inc/Legacy" -I"/home/thepro/Documents/gitrepos/streetlight/streetlight_stm/Drivers/CMSIS/Device/ST/STM32L1xx/Include" -I"/home/thepro/Documents/gitrepos/streetlight/streetlight_stm/Drivers/CMSIS/Include"  -Og -g3 -Wall -fmessage-length=0 -ffunction-sections -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


