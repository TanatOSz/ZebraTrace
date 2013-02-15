#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#	Copyright 2012 Maxim.S.Barabash <maxim.s.barabash@gmail.com>
#
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.


#to trace the image is used PyQt4
#(http://www.riverbankcomputing.co.uk/software/pyqt/download)

from PyQt4.QtGui import QImage, QColor, qGray

GRAYSCALE_COLORTABLE = [QColor(i, i, i).rgb() for i in range(256)]


def grayscale(image):
	image = image.convertToFormat(QImage.Format_Indexed8,
						GRAYSCALE_COLORTABLE)
	return image


def desaterate(image, progress=None):
	p = 100.0 / image.height()
	if not image.isGrayscale():
		for imy in range(image.height()):
			for imx in range(image.width()):
				lightness = qGray(image.pixel(imx, imy))
				image.setPixel(imx, imy,
					(lightness << 16) + (lightness << 8) + lightness)
			if progress: progress(p * imy)
	if progress: progress(0)
	return image