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
	{ 0x907db986, "param_ops_uint" },
	{ 0xfe990052, "gpio_free" },
	{ 0x8a90fa62, "gpiod_unexport" },
	{ 0xf7afa08b, "kthread_stop" },
	{ 0xf70e43a3, "wake_up_process" },
	{ 0x4c39d2df, "kthread_create_on_node" },
	{ 0xfc5528b8, "gpiod_export" },
	{ 0x8e236dea, "gpiod_direction_output_raw" },
	{ 0x47229b5c, "gpio_request" },
	{ 0x56c87b84, "kobject_put" },
	{ 0x4aa4d4ea, "sysfs_create_group" },
	{ 0x868f8b1f, "kobject_create_and_add" },
	{ 0xd09cfa5d, "kernel_kobj" },
	{ 0x86332725, "__stack_chk_fail" },
	{ 0xbcab6ee6, "sscanf" },
	{ 0x8f678b07, "__stack_chk_guard" },
	{ 0x84b183ae, "strncmp" },
	{ 0xf9a482f9, "msleep" },
	{ 0x3f99cd54, "gpiod_set_raw_value" },
	{ 0x7f70363f, "gpio_to_desc" },
	{ 0xb3f7646e, "kthread_should_stop" },
	{ 0xc5850110, "printk" },
	{ 0x3c3ff9fd, "sprintf" },
	{ 0xb1ad28e0, "__gnu_mcount_nc" },
};

MODULE_INFO(depends, "");


MODULE_INFO(srcversion, "7A4FD91238467961732045A");
