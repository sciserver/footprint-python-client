# coding: utf-8
"""
    null

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: null
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import footprint
from footprint import Configuration
from footprint.sciserver_client import SciServerClient
from footprint.api.editor_api import EditorApi  # noqa: E501
from footprint.rest import ApiException
from footprint.models import *
from astropy.io import fits
from astropy.wcs import WCS

class TestEditorApi(unittest.TestCase):
    """EditorApi unit test stubs"""

    def setUp(self):
        self.configuration = Configuration()
        self.configuration.host = "http://localhost/tomshark/footprint-v2.0/Api/"
        self.configuration.proxy = 'http://localhost:8888'
        self.ssclient = SciServerClient(configuration=self.configuration)
        self.api = EditorApi(self.ssclient) # noqa: E501

    def tearDown(self):
        pass

    def test_c_hull_regions(self):
        """Test case for c_hull_regions

        Generate the convex hull of the regions.  # noqa: E501
        """
        r1 = Region()
        r1.region_string = 'Rect J2000 0 0 10 10'
        self.api.create_region("test1", RegionRequest(r1))
        r2 = self.api.get_region("test1").region
         
        req = RegionRequest()
        req.selection = ["test1",]
        self.api.c_hull_regions("test2", req)
        r3 = self.api.get_region("test2").region

        req.selection = ["test2",]
        self.api.c_hull_regions("test3", req)
        r4 = self.api.get_region("test3").region

        self.assertGreaterEqual(r3.area,r2.area)
        self.assertGreaterEqual(r4.area,r3.area)

    def test_copy_region(self):
        """Test case for copy_region

        Copy a region.  # noqa: E501
        """
        r1 = Region()
        r1.region_string = 'Rect J2000 0 0 10 10'
        self.api.create_region("test1", RegionRequest(r1))
        
        req = RegionRequest()
        req.selection = ["test1",]
        self.api.copy_region("test2", req)

        r2 = self.api.get_region("test1").region
        r3 = self.api.get_region("test2").region
        self.assertEqual(r2.area,r3.area)

    def test_create_region(self):
        """Test case for create_region

        Create a new region.  # noqa: E501
        """
        r1 = Region()
        r1.region_string = 'CIRCLE J2000 10 10 10'
        self.api.create_region("test", RegionRequest(r1))
        r2 = self.api.get_region("test").region
        self.assertEqual(0.087266401064508378, r2.area)

        r3 = self.api.create_region("test2", { "region": { "regionString": "CIRCLE J2000 20 20 10"}})
        self.assertEqual(0.08726640106450838, r3.region.area)


    def test_delete_footprint(self):
        """Test case for delete_footprint

        Delete footprint and reset the editor.  # noqa: E501
        """
        r1 = Region()
        r1.region_string = 'CIRCLE J2000 10 10 10'
        r2 = Region()
        r2.region_string = 'CIRCLE J2000 10 10 10'
        r3 = Region()
        r3.region_string = 'CIRCLE J2000 10 10 10'
        self.api.create_region("test1", RegionRequest(r1))
        self.api.create_region("test2", RegionRequest(r2))
        self.api.create_region("test3", RegionRequest(r3))
        req = FootprintRequest()
        req.footprint = Footprint()
        req.footprint.combination_method = CombinationMethod.UNION
        res1 = self.api.list_regions()
        self.api.modify_footprint(req)
        self.api.delete_footprint()
        self.api.list_regions()
        res2 = self.api.list_regions()
        self.assertEqual(len(res2.regions), 0)

    def test_delete_region(self):
        """Test case for delete_region

        Delete a region.  # noqa: E501
        """
        r1 = Region()
        r1.region_string = 'CIRCLE J2000 10 10 10'
        self.api.create_region("test1", RegionRequest(r1))
        self.api.delete_region("test1")
        res = self.api.list_regions()
        self.assertEqual(len(res.regions), 0)
        
        r2 = Region()
        r2.region_string = 'CIRCLE J2000 10 10 10'
        self.api.create_region("test2", RegionRequest(r2))
        self.api.create_region("test1", RegionRequest(r1))
        self.api.delete_region("test1")
        res = self.api.list_regions()
        self.assertEqual(len(res.regions), 1)

    def test_download_footprint(self):
        """Test case for download_footprint

        Returns the footprint in raw format text or binary.  # noqa: E501
        """
        r1 = Region()
        r1.region_string = 'CIRCLE J2000 10 10 10'
        self.api.create_region("test1", RegionRequest(r1))
        r2 = Region()
        r2.region_string = 'CIRCLE J2000 1 1 10'
        self.api.create_region("test2", RegionRequest(r2))
        req = FootprintRequest()
        req.footprint = Footprint()
        req.footprint.combination_method = CombinationMethod.UNION
        self.api.modify_footprint(req)
        outline = self.api.download_footprint(accept="text/plain", _preload_content=False)
        self.assertEqual(outline.data, b'REGION\r\n    CONVEX\r\n        0.9698463103929541 0.17101007166283433 0.17364817766693033 0.99999576920548627\r\n\r\n    CONVEX\r\n        0.99969541350954794 0.017449748351250485 0.017452406437283512 0.99999576920548627\r\n\r\n')
        

    def test_download_footprint_outline(self):
        """Test case for download_footprint_outline

        Returns the outline of the footprint.  # noqa: E501
        """
        r1 = Region()
        r1.region_string = 'CIRCLE J2000 10 10 10'
        self.api.create_region("test1", RegionRequest(r1))
        r2 = Region()
        r2.region_string = 'CIRCLE J2000 20 20 10'
        self.api.create_region("test2", RegionRequest(r2))

        req = FootprintRequest()
        req.footprint = Footprint()
        req.footprint.combination_method = CombinationMethod.UNION
        self.api.modify_footprint(req)
        self.api.download_footprint_outline(accept="text/plain", _preload_content=False)

        self.assertEqual(self.ssclient.last_response.data,b'OUTLINE\r\n    LOOP\r\n        ARC 0.9698463103929541 0.17101007166283433 0.17364817766693033 0.99999576920548627 0.97034732853354255 0.16814466256280783 0.17364744299717294 0.97034732853354255 0.16814466256280783 0.17364744299717294\r\n\r\n    LOOP\r\n        ARC 0.88302222155948906 0.32139380484326968 0.34202014332566871 0.99999576920548627 0.88401338053904255 0.318658993915464 0.34201869630872272 0.88401338053904255 0.318658993915464 0.34201869630872272\r\n\r\n')

    def test_download_region(self):
        """Test case for download_region

        Returns the shape description of the footprint region.  # noqa: E501
        """
        r1 = Region()
        r1.region_string = 'CIRCLE J2000 10 10 10'
        self.api.create_region("test_download_region", RegionRequest(r1))
        self.api.download_region("test_download_region", accept="text/plain", _preload_content=False)
        self.assertEqual(self.ssclient.last_response.data,b'REGION\r\n    CONVEX\r\n        0.9698463103929541 0.17101007166283433 0.17364817766693033 0.99999576920548627\r\n\r\n')

    def test_download_region_outline(self):
        """Test case for download_region_outline

        Returns the outline of the footprint.  # noqa: E501
        """
        r1 = Region()
        r1.region_string = 'CIRCLE J2000 10 10 10'
        self.api.create_region("test_download_region_outline", RegionRequest(r1))
        self.api.download_region_outline("test_download_region_outline", accept="text/plain", _preload_content=False)
        self.assertEqual(self.ssclient.last_response.data, b'OUTLINE\r\n    LOOP\r\n        ARC 0.9698463103929541 0.17101007166283433 0.17364817766693033 0.99999576920548627 0.97034732853354255 0.16814466256280783 0.17364744299717294 0.97034732853354255 0.16814466256280783 0.17364744299717294\r\n\r\n')

    def test_get_footprint(self):
        """Test case for get_footprint

        Returns the header information of the edited footprint  # noqa: E501
        """
        r1 = Region()
        r1.region_string = 'CIRCLE J2000 10 10 10'
        self.api.create_region("test", RegionRequest(r1))
        req = FootprintRequest()
        req.footprint = Footprint()
        req.footprint.combination_method = CombinationMethod.UNION
        self.api.modify_footprint(req)
        
        res = self.api.get_footprint()
        self.assertEqual(res.footprint.name, 'new_footprint')

    def test_get_footprint_outline_points(self):
        """Test case for get_footprint_outline_points

        Returns the points of the outline of the footprint.  # noqa: E501
        """
        r1 = Region()
        r1.region_string = 'CIRCLE J2000 10 10 0.1'
        self.api.create_region("test1", RegionRequest(r1))
        r2 = Region()
        r2.region_string = 'CIRCLE J2000 0 0 0.1'
        self.api.create_region("test2", RegionRequest(r2))
        req = FootprintRequest()
        req.footprint = Footprint()
        req.footprint.combination_method = CombinationMethod.UNION
        self.api.modify_footprint(req)
        points = self.api.get_footprint_outline_points()
        self.assertEqual(self.ssclient.last_response.data, "[{\"lon\":9.9983076222260951,\"lat\":9.9999999957257124},{\"lon\":9.9991538148716028,\"lat\":9.9985566231837328},{\"lon\":10.000846185128445,\"lat\":9.9985566231837328},{\"lon\":10.00169237777399,\"lat\":9.9999999957257124},{\"lon\":10.000846192645945,\"lat\":10.001443374679123},{\"lon\":9.9983076222260951,\"lat\":9.9999999957257124},{\"lon\":359.99833333324716,\"lat\":0.0},{\"lon\":359.99916666662358,\"lat\":-0.0014433757476998812},{\"lon\":0.00083333337639550733,\"lat\":-0.0014433757476998814},{\"lon\":0.0016666667528350855,\"lat\":-2.041010695154396E-19},{\"lon\":0.00083333337639550733,\"lat\":0.001443375747699881},{\"lon\":359.99833333324716,\"lat\":0.0}]")

    def test_get_region(self):
        """Test case for get_region

        Returns the header information of a region.  # noqa: E501
        """
        r1 = Region()
        r1.region_string = 'CIRCLE J2000 10 10 10'
        self.api.create_region("test1", RegionRequest(r1))
        r2 = Region()
        r2.region_string = 'CIRCLE J2000 10 10 11'
        self.api.create_region("test2", RegionRequest(r2))
        self.api.get_region("test1",_preload_content=False)
        self.assertEqual(self.ssclient.last_response.data, b"{\"region\":{\"footprintName\":\"new_footprint\",\"name\":\"test1\",\"fillFactor\":1.0,\"isSimplified\":true,\"area\":0.087266401064508378}}")

    def test_get_region_outline_points(self):
        """Test case for get_region_outline_points

        Returns the points of the outline of the region.  # noqa: E501
        """
        r1 = Region()
        r1.region_string = 'CIRCLE J2000 10 10 0.1'
        self.api.create_region("test", RegionRequest(r1))
        self.api.get_region_outline_points("test")
        self.assertEqual(self.ssclient.last_response.data,"[{\"lon\":9.9983076222260951,\"lat\":9.9999999957257124},{\"lon\":9.9991538148716028,\"lat\":9.9985566231837328},{\"lon\":10.000846185128445,\"lat\":9.9985566231837328},{\"lon\":10.00169237777399,\"lat\":9.9999999957257124},{\"lon\":10.000846192645945,\"lat\":10.001443374679123},{\"lon\":9.9983076222260951,\"lat\":9.9999999957257124}]")

    def test_grow_region(self):
        """Test case for grow_region

        Grow region.  # noqa: E501
        """
        r1 = Region()
        r1.region_string = 'CIRCLE J2000 10 10 10'
        self.api.create_region("test1", RegionRequest(r1))

        req = RegionRequest()
        req.selection = ["test1",]
        req.keep_original = True
        self.api.grow_region("test2", req, radius=1)
        
        r1 = self.api.get_region("test1").region
        r2 = self.api.get_region("test2").region  
        
        self.assertLess(r1.area, r2.area)

    def test_intersect_regions(self):
        """Test case for intersect_regions

        Compute the intersection of regions.  # noqa: E501
        """
        r1 = Region()
        r1.region_string = 'CIRCLE J2000 10 10 200'
        self.api.create_region("test1", RegionRequest(r1))
        r2 = Region()
        r3 = Region()
        r2.region_string = 'CIRCLE J2000 11 11 200'
        self.api.create_region("test2", RegionRequest(r2))
        
        req = RegionRequest()
        req.selection = ["test1", "test2"]
        req.keep_original = True
        self.api.intersect_regions("test3",req)

        r1 = self.api.get_region("test1")
        r2 = self.api.get_region("test2")
        r3 = self.api.get_region("test3")

        self.assertLessEqual(r3.region.area, r1.region.area)
        self.assertLessEqual(r3.region.area, r2.region.area)

    def test_list_regions(self):
        """Test case for list_regions

        List regions.  # noqa: E501
        """
        r1 = Region()
        r1.region_string = 'CIRCLE J2000 10 10 10'
        self.api.create_region("testlist1", RegionRequest(r1))
        self.api.list_regions()
        self.assertEqual(self.ssclient.last_response.data, "{\"regions\":[{\"footprintName\":\"new_footprint\",\"name\":\"testlist1\",\"fillFactor\":1.0,\"isSimplified\":true,\"area\":0.087266401064508378}]}")

        r2 = Region()
        r2.region_string = 'CIRCLE J2000 11 10 10'
        self.api.create_region("testlist2", RegionRequest(r2))
        self.api.list_regions()
        self.assertEqual(self.ssclient.last_response.data, "{\"regions\":[{\"footprintName\":\"new_footprint\",\"name\":\"testlist1\",\"fillFactor\":1.0,\"isSimplified\":true,\"area\":0.087266401064508378},{\"footprintName\":\"new_footprint\",\"name\":\"testlist2\",\"fillFactor\":1.0,\"isSimplified\":true,\"area\":0.087266401064508378}]}")


    def test_modify_footprint(self):
        """Test case for modify_footprint

        Modified the properties of the footprint in the editor.  # noqa: E501
        """
        r1 = Region()
        r1.region_string = 'CIRCLE J2000 10 10 10'
        self.api.create_region("tes1", RegionRequest(r1))
        r2 = Region()
        r2.region_string = 'CIRCLE J2000 11 10 10'
        self.api.create_region("test2", RegionRequest(r2))

        req = FootprintRequest()
        req.footprint = Footprint()
        req.footprint.combination_method = CombinationMethod.UNION

        self.api.modify_footprint(req)
        
        r3 = self.api.get_footprint();
        self.assertEqual(r3.footprint.combination_method, 'union')

        req.footprint.combination_method = CombinationMethod.INTERSECT

        self.api.modify_footprint(req)
        
        r3 = self.api.get_footprint();
        self.assertEqual(r3.footprint.combination_method, 'intersect')

    def test_modify_region(self):
        """Test case for modify_region

        Modify a region.  # noqa: E501
        """
        r1 = Region()
        r1.region_string = 'CIRCLE J2000 10 10 10'
        self.api.create_region("test_mregion1", RegionRequest(r1))
        r2 = Region()
        r2.region_string = 'CIRCLE J2000 20 20 20'
        self.api.modify_region("test_mregion1", RegionRequest(r2))
        self.assertEqual(self.ssclient.last_response.data, "{\"region\":{\"footprintName\":\"new_footprint\",\"name\":\"test_mregion1\",\"fillFactor\":1.0,\"isSimplified\":true,\"area\":0.34906486584773644}}")
        
    def test_rename_region(self):
        """Test case for move_region

        Move a region.  # noqa: E501
        """
        r1 = Region()
        r1.region_string = 'CIRCLE J2000 10 10 10'
        self.api.create_region("test", RegionRequest(r1))
        req = RegionRequest()
        req.selection = ["test",]
        self.api.rename_region("test_rename", req)
        self.api.list_regions()
        self.assertEqual(self.ssclient.last_response.data, "{\"regions\":[{\"footprintName\":\"new_footprint\",\"name\":\"test_rename\",\"fillFactor\":1.0,\"isSimplified\":true,\"area\":0.087266401064508378}]}")

    def test_plot_footprint(self):
        """Test case for plot_footprint

        Plots the footprint  # noqa: E501
        """
        r1 = Region()
        r1.region_string = 'CIRCLE J2000 10 10 100'
        r2 = Region()
        r2.region_string = 'CIRCLE J2000 1 11 110'
        r3 = Region()
        r3.region_string = 'CIRCLE J2000 40 40 400'
        self.api.create_region("test1", RegionRequest(r1))
        self.api.create_region("test2", RegionRequest(r2))
        self.api.create_region("test3", RegionRequest(r3))

        req = FootprintRequest()
        req.footprint = Footprint()
        req.footprint.combination_method = CombinationMethod.UNION
        self.api.modify_footprint(req)

        self.api.plot_region("test1", "image/png", _preload_content=False)
        self.assertEqual("tested","tested")

        self.api.plot_footprint("image/png", _preload_content=False)

    def test_plot_footprint_advanced(self):
        """Test case for plot_footprint_advanced

        Plots the footprint, with advanced parameters  # noqa: E501
        """
#        self.fail()
        r1 = Region()
        r1.region_string = 'CIRCLE J2000 10 10 100'
        r2 = Region()
        r2.region_string = 'CIRCLE J2000 1 11 110'
        r3 = Region()
        r3.region_string = 'CIRCLE J2000 40 40 400'
        self.api.create_region("test1", RegionRequest(r1))
        self.api.create_region("test2", RegionRequest(r2))
        self.api.create_region("test3", RegionRequest(r3))

        req = FootprintRequest()
        req.footprint = Footprint()
        req.footprint.combination_method = CombinationMethod.UNION
        self.api.modify_footprint(req)

        self.api.plot_region("test1", "image/png", _preload_content=False)
        preq = PlotRequest()
        preq.plot = Plot()
        self.api.plot_footprint_advanced(preq, "image/png", _preload_content=False)


    def test_plot_region(self):
        """Test case for plot_region

        Plots the region  # noqa: E501
        """
        r1 = Region()
        r1.region_string = 'CIRCLE J2000 10 10 100'
        r1.region_string = 'RECT J2000 0 0 10 20'
        self.api.create_region("test", RegionRequest(r1))
        
        res = self.api.plot_region("test", accept="image/png", _preload_content=False)
        self.api.plot_region("test", accept='image/jpeg', _preload_content=False)
        self.api.plot_region("test", accept='image/gif', _preload_content=False)
        self.api.plot_region("test", accept='image/bmp', _preload_content=False)
        #self.api.plot_region("test", accept='application/pdf',
        #_preload_content=False)
        #self.api.plot_region("test", accept='application/postscript',
        #_preload_content=False)
        #self.api.plot_region("test", accept='windows/metafile',
        #_preload_content=False)
        self.api.plot_region("test", accept="image/png",projection="GALJ2000", color_theme="green" , _preload_content=False)
        self.assertEqual("tested","tested")


    def test_plot_region_advanced(self):
        """Test case for plot_region_advanced

        Plots the region, with advanced parameters  # noqa: E501
        """
        r1 = Region()
        r1.region_string = 'CIRCLE J2000 10 10 100'
        self.api.create_region("test", RegionRequest(r1))
        preq = PlotRequest()
        preq.plot = Plot()
        self.api.plot_region_advanced("test", preq, "image/png", _preload_content=False)

    def test_subtract_regions(self):
        """Test case for subtract_regions

        Compute the difference of regions.  # noqa: E501
        """
        r1 = Region()
        r1.region_string = 'CIRCLE J2000 10 10 100'
        self.api.create_region("test1", RegionRequest(r1))
        r2 = Region()
        r2.region_string = 'CIRCLE J2000 10.01 10.01 100'
        self.api.create_region("test2", RegionRequest(r2))
        
        req = RegionRequest()
        req.selection = ["test1", "test2"]
        req.keep_original = True
        self.api.subtract_regions("testsubtract",req)

        r1 = self.api.get_region("test1")
        r2 = self.api.get_region("test2")
        r3 = self.api.get_region("testsubtract")

        self.assertLessEqual(r3.region.area, r1.region.area)
        self.assertLessEqual(r3.region.area, r2.region.area)


    def test_union_regions(self):
        """Test case for union_regions

        Compute the union of regions.  # noqa: E501
        """
        r1 = Region()
        r1.region_string = 'CIRCLE J2000 10 10 100'
        self.api.create_region("test1", RegionRequest(r1))
        r2 = Region()
        r2.region_string = 'CIRCLE J2000 20 20 100'
        self.api.create_region("test2", RegionRequest(r2))
        
        req = RegionRequest()
        req.selection = ["test1", "test2"]
        req.keep_original = True
        self.api.union_regions("testunion", req)
        
        r1 = self.api.get_region("test1")
        r2 = self.api.get_region("test2")
        r3 = self.api.get_region("testunion")

        self.assertGreaterEqual(r3.region.area, r1.region.area)
        self.assertGreaterEqual(r3.region.area, r2.region.area)


    def test_upload_region(self):
        """Test case for upload_region

        Upload a region binary or other representation  # noqa: E501
        """
        self.api.upload_region("test", "text/plain", "CIRCLE J2000 10 10 10")
        r = self.api.get_region("test")
        self.assertEqual(0.08726640106450838, r.region.area)

    def test_new_galeq(self):
        r1 = Region()
        r1.region_string = 'POLY J2000 0 0 0 10 20 0'
        self.api.create_region("eqtest", RegionRequest(r1))

        r2 = Region()
        r2.region_string = 'POLY J2000 0 0 0 10 20 0'
        self.api.create_region("eqtest2", RegionRequest(r2))

        req = RegionRequest(r1)
        req.sys = CoordinateSystem.GALJ2000
        self.api.modify_region("eqtest",req)

        reqf = FootprintRequest()
        reqf.footprint = Footprint()
        reqf.footprint.combination_method = CombinationMethod.UNION
        self.api.modify_footprint(reqf)

#        self.api.plot_footprint("image/png", _preload_content=False)

        preq = PlotRequest()
        preq.plot = Plot()
#        self.api.plot_region("eqtest",  "image/png", projection = "GalJ2000", auto_zoom = False, color_theme = "blue", _preload_content=False)
        self.api.plot_region("eqtest", "image/png", sys = "GALJ2000", auto_zoom = False, color_theme = "blue", _preload_content=False)

    def test_new_galeq2(self):
        r1 = Region()
        r1.region_string = 'CONVEX 0.9698463103929541 0.17101007166283433 0.17364817766693033 0.9995769500822006'
        req = RegionRequest(r1)
        req.sys = CoordinateSystem.GALJ2000
        self.api.create_region("eqtest1", req)

        r2 = Region()
        r2.region_string = 'CIRCLE J2000 10 10 100'
        self.api.create_region("eqtest2", RegionRequest(r2))

        reqf = FootprintRequest()
        reqf.footprint = Footprint()
        reqf.footprint.combination_method = CombinationMethod.UNION
        self.api.modify_footprint(reqf)

        self.api.plot_footprint("image/png", _preload_content=False)
        self.api.download_region("eqtest1", accept="text/plain", _preload_content=False)
        self.api.get_region("eqtest1",_preload_content=False)

    def test_new_rotation(self):
        r1 = Region()
        r1.region_string = 'POLY J2000 0 0 0 10 20 0'
        req = RegionRequest(r1)
        alp = Rotation()
        alp.alpha = 20
        alp.beta = 0
        alp.gamma = 0
        req.rotation = alp
        self.api.create_region("eqtest", req)
        self.api.plot_region("eqtest",  "image/png",  _preload_content=False)

    def test_modify_rot(self):
        r1 = Region()
        r1.region_string = 'POLY J2000 0 0 0 10 20 0'
        req = RegionRequest(r1)
        alp = Rotation()
        alp.alpha = 20
        alp.beta = 0
        alp.gamma = 0
        req.rotation = alp
        self.api.create_region("modrottest", RegionRequest(r1))
        self.api.create_region("modrottestinit", RegionRequest(r1))
        self.api.modify_region("modrottest", req)
        self.api.plot_region("modrottest",  "image/png",  _preload_content=False)
        self.api.plot_region("modrottestinit",  "image/png",  _preload_content=False)

    def test_modify_rot2(self):
        r1 = Region()
        r1.region_string = 'POLY J2000 0 0 0 10 20 0'
        req = RegionRequest(r1)
        alp = Rotation()
        alp.alpha = 20
        alp.beta = 0
        alp.gamma = 0
        req.rotation = alp
        self.api.create_region("test1", req)
        self.api.get_region("test1",_preload_content=False)
        respget1 = self.ssclient.last_response.data
        self.api.download_region("test1", accept="text/plain", _preload_content=False)
        respdow1 = self.ssclient.last_response.data

        self.api.delete_region("test1")

        r2 = Region()
        r2.region_string = 'POLY J2000 0 0 0 10 20 0'
        req = RegionRequest(r2)
        alp = Rotation()
        alp.alpha = 20
        alp.beta = 0
        alp.gamma = 0
        req.rotation = alp
        self.api.create_region("test1", RegionRequest(r2))
        self.api.modify_region("test1", req)
        self.api.get_region("test1",_preload_content=False)
        respget2 = self.ssclient.last_response.data
        self.api.download_region("test1", accept="text/plain", _preload_content=False)
        respdow2 = self.ssclient.last_response.data

        self.assertEqual(respget1,respget2)
        self.assertEqual(respdow1,respdow2)

    def test_new_astropy_two_image(self):
        filename1 = "C:/Users/tomshark/Downloads/hspireplw1342246580_20pmp_1463459088096.fits"
        filename2 = "C:/Users/tomshark/Downloads/hspireplw1342237553_20pmp_1463454955470.fits"
        w1 = WCS(filename1)
        w2 = WCS(filename2)
        image1 = fits.open(filename1)
        image2 = fits.open(filename2)

        #store header
        header1 = image1[1].header
        header2 = image2[1].header
        n1 = header1["NAXIS1"]
        m1 = header1["NAXIS2"]

        lon1, lat1 = w1.all_pix2world(0, 0, 0)
        lon2, lat2 = w1.all_pix2world(n1, 0, 0)
        lon3, lat3 = w1.all_pix2world(n1, m1, 0)
        lon4, lat4 = w1.all_pix2world(0, m1, 0)
        r1 = Region()
        r1.region_string = 'POLY J2000 ' + str(lon1) + ' ' + str(lat1) + ' ' + str(lon2) + ' ' + str(lat2) + ' ' + str(lon3) + ' ' + str(lat3) + ' ' + str(lon4) + ' ' + str(lat4) 
        #r1.region_string = 'POLY J2000 ' + str(lon1, lat1) + ' ' + str(lon2, lat2) + ' ' + str(lon3, lat3) + ' ' + str(lon4, lat4) 

        header2 = image2[1].header
        n1 = header2["NAXIS1"]
        m1 = header2["NAXIS2"]
        lon1, lat1 = w2.all_pix2world(0, 0, 0)
        lon2, lat2 = w2.all_pix2world(n1, 0, 0)
        lon3, lat3 = w2.all_pix2world(n1, m1, 0)
        lon4, lat4 = w2.all_pix2world(0, m1, 0)
        r2 = Region()
        r2.region_string = 'POLY J2000 ' + str(lon1) + ' ' + str(lat1) + ' ' + str(lon2) + ' ' + str(lat2) + ' ' + str(lon3) + ' ' + str(lat3) + ' ' + str(lon4) + ' ' + str(lat4) 

        self.api.create_region("test1", RegionRequest(r1))
        self.api.create_region("test2", RegionRequest(r2))

        res = self.api.plot_region("test1", accept="image/png", _preload_content=False)
        req = FootprintRequest()
        req.footprint = Footprint()
        req.footprint.combination_method = CombinationMethod.UNION
        self.api.modify_footprint(req)

        self.api.plot_footprint("image/png", _preload_content=False)

        rreq = RegionRequest()
        rreq.selection = ["test1", "test2"]
        rreq.keep_original = True
        self.api.union_regions("testunion", rreq)
        
        r1 = self.api.get_region("test1")
        r2 = self.api.get_region("test2")
        r3 = self.api.get_region("testunion")

        self.assertGreaterEqual(r3.region.area, r1.region.area)
        self.assertGreaterEqual(r3.region.area, r2.region.area)

    def test_new_two_image(self):
        #read fits
        filename1 = "C:/Users/tomshark/Downloads/hspireplw1342246580_20pmp_1463459088096.fits"
        filename2 = "C:/Users/tomshark/Downloads/hspireplw1342237553_20pmp_1463454955470.fits"
        
        image1 = fits.open(filename1)
        image2 = fits.open(filename2)

        #store header
        header1 = image1[1].header
        #read different parameters from header
        n1 = header1["NAXIS1"]
        m1 = header1["NAXIS2"]
        centerx1 = header1["CRPIX1"]
        centery1 = header1["CRPIX2"]
        center_ra1 = header1["CRVAL1"]
        center_dec1 = header1["CRVAL2"]
        pix_to_degree1x = header1["CDELT2"]
        pix_to_degree1y = header1["CDELT2"]
        rot1 = header1["CROTA2"]

        if centerx1 - round(centerx1) == 0:
            buttomleftcrx = center_ra1 - (centerx1) * pix_to_degree1x
            buttomleftcry = center_dec1 - (centery1) * pix_to_degree1y
        else:
            buttomleftcrx = center_ra1 - (centerx1 - 0.5) * pix_to_degree1x
            buttomleftcry = center_dec1 - (centery1 - 0.5) * pix_to_degree1y

        a1 = pix_to_degree1x * n1 + buttomleftcrx
        b1 = pix_to_degree1y * m1 + buttomleftcry

        r1 = Region()
        r1.region_string = 'POLY J2000 ' + str(buttomleftcrx) + ' ' +str(buttomleftcry) + ' ' +str(buttomleftcrx+a1) + ' ' + str(buttomleftcry) + ' ' + str(buttomleftcrx+a1) + ' ' + str(buttomleftcry+b1) + ' ' + str(buttomleftcrx) + ' ' + str(buttomleftcry+b1)
        #r1.region_string = 'POLY J2000  0 0 10 10 0 10'
        #r1.region_string = 'RECT J2000 5 0 10 10'
        self.api.create_region("test1", RegionRequest(r1))

        #store header
        header2 = image2[1].header
        #read different parameters from header
        n2 = header2["NAXIS1"]
        m2 = header2["NAXIS2"]
        centerx2 = header2["CRPIX1"]
        centery2 = header2["CRPIX2"]
        center_ra2 = header2["CRVAL1"]
        center_dec2 = header2["CRVAL2"]
        pix_to_degree2x = header2["CDELT2"]
        pix_to_degree2y = header2["CDELT2"]
        rot2 = header2["CROTA2"]

        if centerx2 - round(centerx2) == 0:
            buttomleftcrx = center_ra2 - (centerx2) * pix_to_degree2x
            buttomleftcry = center_dec2 - (centery2) * pix_to_degree2y
        else:
            buttomleftcrx = center_ra2 - (centerx1 - 0.5) * pix_to_degree2x
            buttomleftcry = center_dec2 - (centery1 - 0.5) * pix_to_degree2y

        a2 = pix_to_degree2x * n2 + buttomleftcrx
        b2 = pix_to_degree2y * m2 + buttomleftcry

        r2 = Region()
        r2.region_string = 'POLY J2000 ' + str(buttomleftcrx) + ' ' +str(buttomleftcry) + ' ' +str(buttomleftcrx+a2) + ' ' + str(buttomleftcry) + ' ' + str(buttomleftcrx+a2) + ' ' + str(buttomleftcry+b2) + ' ' + str(buttomleftcrx) + ' ' + str(buttomleftcry+b2)

        self.api.create_region("test2", RegionRequest(r2))
        
        #res = self.api.plot_region("test", accept="image/png", _preload_content=False)
        
        req = FootprintRequest()
        req.footprint = Footprint()
        req.footprint.combination_method = CombinationMethod.UNION
        self.api.modify_footprint(req)

        self.api.plot_footprint("image/png", _preload_content=False)

if __name__ == '__main__':
    unittest.main()
