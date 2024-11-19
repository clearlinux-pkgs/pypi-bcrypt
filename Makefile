PKG_NAME := pypi-bcrypt
URL = https://files.pythonhosted.org/packages/56/8c/dd696962612e4cd83c40a9e6b3db77bfe65a830f4b9af44098708584686c/bcrypt-4.2.1.tar.gz
ARCHIVES = $(CGIT_BASE_URL)/vendor/pypi-bcrypt/snapshot/pypi-bcrypt-2024-07-23-00-41-12.tar.xz ./vendor $(CGIT_BASE_URL)/vendor/pypi-bcrypt/snapshot/pypi-bcrypt-2024-11-19-21-16-18.tar.gz ./vendor

include ../common/Makefile.common
