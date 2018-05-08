# coding: utf-8

"""
    null

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: null
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from footprint.models.color_theme import ColorTheme  # noqa: F401,E501
from footprint.models.coordinate_system import CoordinateSystem  # noqa: F401,E501
from footprint.models.degree_style import DegreeStyle  # noqa: F401,E501
from footprint.models.projection import Projection  # noqa: F401,E501


class Plot(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'width': 'float',
        'height': 'float',
        'theme': 'ColorTheme',
        'proj': 'Projection',
        'sys': 'CoordinateSystem',
        'lon': 'float',
        'lat': 'float',
        'zoom': 'bool',
        'rotate': 'bool',
        'grid': 'bool',
        'grid_density': 'float',
        'grid_sys': 'CoordinateSystem',
        'axes_visible': 'bool',
        'axis_labels_visible': 'bool',
        'degree_style': 'DegreeStyle',
        'font_size': 'int',
        'line_width': 'int',
        'regions_visible': 'bool',
        'outline_visible': 'bool'
    }

    attribute_map = {
        'width': 'width',
        'height': 'height',
        'theme': 'theme',
        'proj': 'proj',
        'sys': 'sys',
        'lon': 'lon',
        'lat': 'lat',
        'zoom': 'zoom',
        'rotate': 'rotate',
        'grid': 'grid',
        'grid_density': 'gridDensity',
        'grid_sys': 'gridSys',
        'axes_visible': 'axesVisible',
        'axis_labels_visible': 'axisLabelsVisible',
        'degree_style': 'degreeStyle',
        'font_size': 'fontSize',
        'line_width': 'lineWidth',
        'regions_visible': 'regionsVisible',
        'outline_visible': 'outlineVisible'
    }

    def __init__(self, width=None, height=None, theme=None, proj=None, sys=None, lon=None, lat=None, zoom=None, rotate=None, grid=None, grid_density=None, grid_sys=None, axes_visible=None, axis_labels_visible=None, degree_style=None, font_size=None, line_width=None, regions_visible=None, outline_visible=None):  # noqa: E501
        """Plot - a model defined in Swagger"""  # noqa: E501

        self._width = None
        self._height = None
        self._theme = None
        self._proj = None
        self._sys = None
        self._lon = None
        self._lat = None
        self._zoom = None
        self._rotate = None
        self._grid = None
        self._grid_density = None
        self._grid_sys = None
        self._axes_visible = None
        self._axis_labels_visible = None
        self._degree_style = None
        self._font_size = None
        self._line_width = None
        self._regions_visible = None
        self._outline_visible = None
        self.discriminator = None

        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if theme is not None:
            self.theme = theme
        if proj is not None:
            self.proj = proj
        if sys is not None:
            self.sys = sys
        if lon is not None:
            self.lon = lon
        if lat is not None:
            self.lat = lat
        if zoom is not None:
            self.zoom = zoom
        if rotate is not None:
            self.rotate = rotate
        if grid is not None:
            self.grid = grid
        if grid_density is not None:
            self.grid_density = grid_density
        if grid_sys is not None:
            self.grid_sys = grid_sys
        if axes_visible is not None:
            self.axes_visible = axes_visible
        if axis_labels_visible is not None:
            self.axis_labels_visible = axis_labels_visible
        if degree_style is not None:
            self.degree_style = degree_style
        if font_size is not None:
            self.font_size = font_size
        if line_width is not None:
            self.line_width = line_width
        if regions_visible is not None:
            self.regions_visible = regions_visible
        if outline_visible is not None:
            self.outline_visible = outline_visible

    @property
    def width(self):
        """Gets the width of this Plot.  # noqa: E501


        :return: The width of this Plot.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Plot.


        :param width: The width of this Plot.  # noqa: E501
        :type: float
        """

        self._width = width

    @property
    def height(self):
        """Gets the height of this Plot.  # noqa: E501


        :return: The height of this Plot.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Plot.


        :param height: The height of this Plot.  # noqa: E501
        :type: float
        """

        self._height = height

    @property
    def theme(self):
        """Gets the theme of this Plot.  # noqa: E501


        :return: The theme of this Plot.  # noqa: E501
        :rtype: ColorTheme
        """
        return self._theme

    @theme.setter
    def theme(self, theme):
        """Sets the theme of this Plot.


        :param theme: The theme of this Plot.  # noqa: E501
        :type: ColorTheme
        """

        self._theme = theme

    @property
    def proj(self):
        """Gets the proj of this Plot.  # noqa: E501


        :return: The proj of this Plot.  # noqa: E501
        :rtype: Projection
        """
        return self._proj

    @proj.setter
    def proj(self, proj):
        """Sets the proj of this Plot.


        :param proj: The proj of this Plot.  # noqa: E501
        :type: Projection
        """

        self._proj = proj

    @property
    def sys(self):
        """Gets the sys of this Plot.  # noqa: E501


        :return: The sys of this Plot.  # noqa: E501
        :rtype: CoordinateSystem
        """
        return self._sys

    @sys.setter
    def sys(self, sys):
        """Sets the sys of this Plot.


        :param sys: The sys of this Plot.  # noqa: E501
        :type: CoordinateSystem
        """

        self._sys = sys

    @property
    def lon(self):
        """Gets the lon of this Plot.  # noqa: E501


        :return: The lon of this Plot.  # noqa: E501
        :rtype: float
        """
        return self._lon

    @lon.setter
    def lon(self, lon):
        """Sets the lon of this Plot.


        :param lon: The lon of this Plot.  # noqa: E501
        :type: float
        """

        self._lon = lon

    @property
    def lat(self):
        """Gets the lat of this Plot.  # noqa: E501


        :return: The lat of this Plot.  # noqa: E501
        :rtype: float
        """
        return self._lat

    @lat.setter
    def lat(self, lat):
        """Sets the lat of this Plot.


        :param lat: The lat of this Plot.  # noqa: E501
        :type: float
        """

        self._lat = lat

    @property
    def zoom(self):
        """Gets the zoom of this Plot.  # noqa: E501


        :return: The zoom of this Plot.  # noqa: E501
        :rtype: bool
        """
        return self._zoom

    @zoom.setter
    def zoom(self, zoom):
        """Sets the zoom of this Plot.


        :param zoom: The zoom of this Plot.  # noqa: E501
        :type: bool
        """

        self._zoom = zoom

    @property
    def rotate(self):
        """Gets the rotate of this Plot.  # noqa: E501


        :return: The rotate of this Plot.  # noqa: E501
        :rtype: bool
        """
        return self._rotate

    @rotate.setter
    def rotate(self, rotate):
        """Sets the rotate of this Plot.


        :param rotate: The rotate of this Plot.  # noqa: E501
        :type: bool
        """

        self._rotate = rotate

    @property
    def grid(self):
        """Gets the grid of this Plot.  # noqa: E501


        :return: The grid of this Plot.  # noqa: E501
        :rtype: bool
        """
        return self._grid

    @grid.setter
    def grid(self, grid):
        """Sets the grid of this Plot.


        :param grid: The grid of this Plot.  # noqa: E501
        :type: bool
        """

        self._grid = grid

    @property
    def grid_density(self):
        """Gets the grid_density of this Plot.  # noqa: E501


        :return: The grid_density of this Plot.  # noqa: E501
        :rtype: float
        """
        return self._grid_density

    @grid_density.setter
    def grid_density(self, grid_density):
        """Sets the grid_density of this Plot.


        :param grid_density: The grid_density of this Plot.  # noqa: E501
        :type: float
        """

        self._grid_density = grid_density

    @property
    def grid_sys(self):
        """Gets the grid_sys of this Plot.  # noqa: E501


        :return: The grid_sys of this Plot.  # noqa: E501
        :rtype: CoordinateSystem
        """
        return self._grid_sys

    @grid_sys.setter
    def grid_sys(self, grid_sys):
        """Sets the grid_sys of this Plot.


        :param grid_sys: The grid_sys of this Plot.  # noqa: E501
        :type: CoordinateSystem
        """

        self._grid_sys = grid_sys

    @property
    def axes_visible(self):
        """Gets the axes_visible of this Plot.  # noqa: E501


        :return: The axes_visible of this Plot.  # noqa: E501
        :rtype: bool
        """
        return self._axes_visible

    @axes_visible.setter
    def axes_visible(self, axes_visible):
        """Sets the axes_visible of this Plot.


        :param axes_visible: The axes_visible of this Plot.  # noqa: E501
        :type: bool
        """

        self._axes_visible = axes_visible

    @property
    def axis_labels_visible(self):
        """Gets the axis_labels_visible of this Plot.  # noqa: E501


        :return: The axis_labels_visible of this Plot.  # noqa: E501
        :rtype: bool
        """
        return self._axis_labels_visible

    @axis_labels_visible.setter
    def axis_labels_visible(self, axis_labels_visible):
        """Sets the axis_labels_visible of this Plot.


        :param axis_labels_visible: The axis_labels_visible of this Plot.  # noqa: E501
        :type: bool
        """

        self._axis_labels_visible = axis_labels_visible

    @property
    def degree_style(self):
        """Gets the degree_style of this Plot.  # noqa: E501


        :return: The degree_style of this Plot.  # noqa: E501
        :rtype: DegreeStyle
        """
        return self._degree_style

    @degree_style.setter
    def degree_style(self, degree_style):
        """Sets the degree_style of this Plot.


        :param degree_style: The degree_style of this Plot.  # noqa: E501
        :type: DegreeStyle
        """

        self._degree_style = degree_style

    @property
    def font_size(self):
        """Gets the font_size of this Plot.  # noqa: E501


        :return: The font_size of this Plot.  # noqa: E501
        :rtype: int
        """
        return self._font_size

    @font_size.setter
    def font_size(self, font_size):
        """Sets the font_size of this Plot.


        :param font_size: The font_size of this Plot.  # noqa: E501
        :type: int
        """

        self._font_size = font_size

    @property
    def line_width(self):
        """Gets the line_width of this Plot.  # noqa: E501


        :return: The line_width of this Plot.  # noqa: E501
        :rtype: int
        """
        return self._line_width

    @line_width.setter
    def line_width(self, line_width):
        """Sets the line_width of this Plot.


        :param line_width: The line_width of this Plot.  # noqa: E501
        :type: int
        """

        self._line_width = line_width

    @property
    def regions_visible(self):
        """Gets the regions_visible of this Plot.  # noqa: E501


        :return: The regions_visible of this Plot.  # noqa: E501
        :rtype: bool
        """
        return self._regions_visible

    @regions_visible.setter
    def regions_visible(self, regions_visible):
        """Sets the regions_visible of this Plot.


        :param regions_visible: The regions_visible of this Plot.  # noqa: E501
        :type: bool
        """

        self._regions_visible = regions_visible

    @property
    def outline_visible(self):
        """Gets the outline_visible of this Plot.  # noqa: E501


        :return: The outline_visible of this Plot.  # noqa: E501
        :rtype: bool
        """
        return self._outline_visible

    @outline_visible.setter
    def outline_visible(self, outline_visible):
        """Sets the outline_visible of this Plot.


        :param outline_visible: The outline_visible of this Plot.  # noqa: E501
        :type: bool
        """

        self._outline_visible = outline_visible

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Plot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other