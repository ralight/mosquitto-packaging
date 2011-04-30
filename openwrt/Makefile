#
# Copyright (C) 2010 Jo-Philipp Wich <xm@subsignal.org>
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=mosquitto
PKG_VERSION:=0.10
PKG_RELEASE:=1

PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tar.gz
PKG_SOURCE_URL:=http://mosquitto.org/files/source/
PKG_MD5SUM:=245be3e2ed52a8bc7d0da07584a544ab

include $(INCLUDE_DIR)/package.mk

define Package/mosquitto/default
  SECTION:=net
  CATEGORY:=Network
  TITLE:=mosquitto - an MQTT message broker
endef

define Package/mosquitto
  $(Package/mosquitto/default)
  MENU:=1
endef

define Package/mosquitto/description
 mosquitto is a message broker that supports version 3.1 of the MQ Telemetry
 Transport protocol. MQTT provides a lightweight method of carrying out
 messaging using a publish/subscribe model.
endef


#define Build/Prepare
	#mkdir -p $(PKG_BUILD_DIR)
	#$(CP) ./src/* $(PKG_BUILD_DIR)/
#endef

define Package/mosquitto/conffiles
/etc/mosquitto/mosquitto.conf
endef

define Package/mosquitto/install
	$(INSTALL_DIR) $(1)/usr/sbin
	$(INSTALL_BIN) $(PKG_BUILD_DIR)/src/mosquitto $(1)/usr/sbin/mosquitto
	$(INSTALL_DIR) $(1)/etc/mosquitto
	$(INSTALL_CONF) $(PKG_BUILD_DIR)/mosquitto.conf $(1)/etc/mosquitto/mosquitto.conf
endef

$(eval $(call BuildPackage,mosquitto))
