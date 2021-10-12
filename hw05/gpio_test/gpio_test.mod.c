#include <linux/module.h>
#define INCLUDE_VERMAGIC
#include <linux/build-salt.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

BUILD_SALT;

MODULE_INFO(vermagic, VERMAGIC_STRING);
MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__section(".gnu.linkonce.this_module") = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

#ifdef CONFIG_RETPOLINE
MODULE_INFO(retpoline, "Y");
#endif

static const struct modversion_info ____versions[]
__used __section("__versions") = {
	{ 0x71f5d042, "module_layout" },
	{ 0xfe990052, "gpio_free" },
	{ 0xc1514a3b, "free_irq" },
	{ 0x8a90fa62, "gpiod_unexport" },
	{ 0x92d5838e, "request_threaded_irq" },
	{ 0x6328bfde, "gpiod_to_irq" },
	{ 0x48005809, "gpiod_set_debounce" },
	{ 0xc9b3c1e, "gpiod_direction_input" },
	{ 0xfc5528b8, "gpiod_export" },
	{ 0x8e236dea, "gpiod_direction_output_raw" },
	{ 0x47229b5c, "gpio_request" },
	{ 0xc5850110, "printk" },
	{ 0x3f99cd54, "gpiod_set_raw_value" },
	{ 0x4ab0c1ad, "gpiod_get_raw_value" },
	{ 0x7f70363f, "gpio_to_desc" },
	{ 0xb1ad28e0, "__gnu_mcount_nc" },
};

MODULE_INFO(depends, "");


MODULE_INFO(srcversion, "474DED0F14DCF36A812FE24");
