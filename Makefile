PKG_NAME := pypi-bcrypt
URL = https://files.pythonhosted.org/packages/bb/5d/6d7433e0f3cd46ce0b43cd65e1db465ea024dbb8216fb2404e919c2ad77b/bcrypt-4.3.0.tar.gz
ARCHIVES = $(CGIT_BASE_URL)/vendor/pypi-bcrypt/snapshot/pypi-bcrypt-2024-07-23-00-41-12.tar.xz ./vendor $(CGIT_BASE_URL)/vendor/pypi-bcrypt/snapshot/pypi-bcrypt-2025-02-28-15-15-14.tar.gz ./vendor

include ../common/Makefile.common
