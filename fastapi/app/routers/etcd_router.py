import etcd3
from fastapi import APIRouter

router = APIRouter()

etcd_client = etcd3.client(host='etcd', port=2379)
