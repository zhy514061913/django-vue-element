# -*- coding: utf-8 -*-
#author:laoseng(QQ:1572665580),feilong(hhr66@qq.com)
#create:2018-09
# view 业务控制
#from stree.serializers import SimpleStreeSerializer
from utils.base_mixin import ImportMixin, ExportMixin
from utils.base_view import BaseModelViewSet

from .filters import *
from .models import *
from .resources import *
from .serializers import *

logger = logging.getLogger('views')


class IdcViewSet(ImportMixin, ExportMixin, BaseModelViewSet):
    queryset = Idc.objects.order_by('-id')
    serializer_class = IdcSerializer
    ordering_fields = ('id', 'name',)
    search_fields = ('name', 'cname', 'phone', 'network', 'address', 'contact')
    resource_class = IdcResource

class HostViewSet(ImportMixin, ExportMixin, BaseModelViewSet):
    queryset = Host.objects.order_by('-id')
    serializer_class = HostSerializer
    ordering_fields = ('id', 'hostname', 'ip')
    search_fields = ('hostname', 'ip', 'sn', 'manage_ip', 'public_ip', 'other_ip', 'asset_no', 'model')
    filterset_class = HostFilter
    resource_class = HostResource