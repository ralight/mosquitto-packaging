#
# Copyright (C) 2010 Jo-Philipp Wich <xm@subsignal.org>
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=mosquitto
PKG_VERSION:=0.11.3
PKG_RELEASE:=1

PKG_SOURCE:=$(PKG_NAME)-$(PKG_VERSION).tar.gz
PKG_SOURCE_URL:=http://mosquitto.org/files/source/
PKG_MD5SUM:=b322dcaf56d0d1bf8b5b657ab9aa2f06

include $(INCLUDE_DIR)/package.mk

define Package/mosquitto/default
  SECTION:=net
  CATEGORY:=Network
  TITLE:=mosquitto - an MQTT message broker
  URL:=http://www.mosquitto.org/
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

define Package/mosquitto-client
    $(Package/mosquitto/default)
    TITLE:= Command line client tools for MQTT brokers
    DEPENDS:=libmosquitto
endef

define Package/mosquitto-client/description
 Client tools for publishing messages to MQTT servers, and subscribing to topics
endef

define Package/libmosquitto
    $(Package/mosquitto/default)
    TITLE+= (library for third party software)
    DEPENDS:=mosquitto
endef

define Package/libmosquitto/description
 Library required for client tools, and any third party software that communicates via mqtt
endef


define Package/mosquitto/conffiles
/etc/mosquitto/mosquitto.conf
endef

define Package/mosquitto/install
	$(INSTALL_DIR) $(1)/usr/sbin
	$(INSTALL_BIN) $(PKG_BUILD_DIR)/src/mosquitto $(1)/usr/sbin/mosquitto
	$(INSTALL_DIR) $(1)/etc/mosquitto
	$(INSTALL_CONF) $(PKG_BUILD_DIR)/mosquitto.conf $(1)/etc/mosquitto/mosquitto.conf
endef

define Package/mosquitto-client/install
	$(INSTALL_DIR) $(1)/usr/bin
	$(INSTALL_BIN) $(PKG_BUILD_DIR)/client/mosquitto_pub $(1)/usr/bin/mosquitto_pub
	$(INSTALL_BIN) $(PKG_BUILD_DIR)/client/mosquitto_sub $(1)/usr/bin/mosquitto_sub
endef

define Package/libmosquitto/install
	$(INSTALL_DIR) $(1)/usr/lib
	$(INSTALL_BIN) $(PKG_BUILD_DIR)/lib/libmosquitto.so.0 $(1)/usr/lib/libmosquitto.so.0
endef
$(eval $(call BuildPackage,mosquitto))
$(eval $(call BuildPackage,libmosquitto))
$(eval $(call BuildPackage,mosquitto-client))
