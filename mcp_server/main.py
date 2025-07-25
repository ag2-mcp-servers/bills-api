# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T08:15:13+00:00



import argparse
import json
import os
from datetime import datetime
from typing import *
from typing import Optional, Union

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import BaseSecurity
from fastapi import Path, Query

from models import (
    AmendmentDetail,
    AmendmentSearchItemSearchResult,
    Bill,
    BillIds,
    BillPublicationList,
    BillSortOrder,
    BillStage,
    BillStageDetails,
    BillStagePublicationList,
    BillStagesExcluded,
    BillStageSittingSearchResult,
    BillSummarySearchResult,
    BillType1,
    BillTypeCategory,
    BillTypeSearchResult,
    Decision,
    House,
    NewsArticlesSummarySearchResult,
    OriginatingHouse,
    ProblemDetails,
    PublicationDocument,
    PublicationTypeSearchResult,
    StageReferenceSearchResult,
    StageSummarySearchResult,
)

app = MCPProxy(
    contact={
        'email': 'softwareengineering@parliament.uk',
        'name': 'UK Parliament',
        'url': 'https://www.parliament.uk',
    },
    description='API to get and search for information regarding Bills, their stages, associated amendments and publications.',
    title='Bills API',
    version='v1',
    servers=[{'url': 'https://bills-api.parliament.uk'}],
)


@app.get('/api/v1/BillTypes', tags=['bill_management'])
def get_api_v1__bill_types(
    category: Optional[BillTypeCategory] = Query(None, alias='Category'),
    skip: Optional[int] = Query(None, alias='Skip'),
    take: Optional[int] = Query(None, alias='Take'),
):
    """
    Returns a list of Bill types.
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get('/api/v1/Bills', tags=['bill_management', 'bill_stage_management'])
def get_bills(
    search_term: Optional[str] = Query(None, alias='SearchTerm'),
    session: Optional[int] = Query(None, alias='Session'),
    current_house: Optional[House] = Query(None, alias='CurrentHouse'),
    originating_house: Optional[OriginatingHouse] = Query(
        None, alias='OriginatingHouse'
    ),
    member_id: Optional[int] = Query(None, alias='MemberId'),
    department_id: Optional[int] = Query(None, alias='DepartmentId'),
    bill_stage: Optional[BillStage] = Query(None, alias='BillStage'),
    bill_stages_excluded: Optional[BillStagesExcluded] = Query(
        None, alias='BillStagesExcluded'
    ),
    is_defeated: Optional[bool] = Query(None, alias='IsDefeated'),
    is_withdrawn: Optional[bool] = Query(None, alias='IsWithdrawn'),
    bill_type: Optional[BillType1] = Query(None, alias='BillType'),
    sort_order: Optional[BillSortOrder] = Query(None, alias='SortOrder'),
    bill_ids: Optional[BillIds] = Query(None, alias='BillIds'),
    skip: Optional[int] = Query(None, alias='Skip'),
    take: Optional[int] = Query(None, alias='Take'),
):
    """
    Returns a list of Bills.
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get('/api/v1/Bills/{billId}', tags=['bill_management'])
def get_bill(bill_id: int = Path(..., alias='billId')):
    """
    Return a Bill.
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/api/v1/Bills/{billId}/NewsArticles',
    tags=['bill_management', 'news_and_publication_management'],
)
def get_news_articles(
    bill_id: int = Path(..., alias='billId'),
    skip: Optional[int] = Query(None, alias='Skip'),
    take: Optional[int] = Query(None, alias='Take'),
):
    """
    Returns a list of news articles for a Bill.
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/api/v1/Bills/{billId}/Publications',
    tags=['bill_management', 'news_and_publication_management'],
)
def get_bill_publication(bill_id: int = Path(..., alias='billId')):
    """
    Return a list of Bill publications.
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/api/v1/Bills/{billId}/Stages', tags=['bill_management', 'bill_stage_management']
)
def get_api_v1__bills__bill_id__stages(
    bill_id: int = Path(..., alias='billId'),
    skip: Optional[int] = Query(None, alias='Skip'),
    take: Optional[int] = Query(None, alias='Take'),
):
    """
    Returns all Bill stages.
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/api/v1/Bills/{billId}/Stages/{billStageId}',
    tags=['bill_management', 'bill_stage_management'],
)
def get_bill_stage_details(
    bill_id: int = Path(..., alias='billId'),
    bill_stage_id: int = Path(..., alias='billStageId'),
):
    """
    Returns a Bill stage.
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/api/v1/Bills/{billId}/Stages/{billStageId}/Amendments',
    tags=['bill_management', 'bill_stage_management'],
)
def get_amendments(
    bill_id: int = Path(..., alias='billId'),
    bill_stage_id: int = Path(..., alias='billStageId'),
    search_term: Optional[str] = Query(None, alias='SearchTerm'),
    decision: Optional[Decision] = Query(None, alias='Decision'),
    member_id: Optional[int] = Query(None, alias='MemberId'),
    skip: Optional[int] = Query(None, alias='Skip'),
    take: Optional[int] = Query(None, alias='Take'),
):
    """
    Returns a list of amendments.
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/api/v1/Bills/{billId}/Stages/{billStageId}/Amendments/{amendmentId}',
    tags=['bill_management', 'bill_stage_management'],
)
def get_amendment(
    bill_id: int = Path(..., alias='billId'),
    bill_stage_id: int = Path(..., alias='billStageId'),
    amendment_id: int = Path(..., alias='amendmentId'),
):
    """
    Returns an amendment.
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/api/v1/Bills/{billId}/Stages/{stageId}/Publications',
    tags=[
        'bill_management',
        'bill_stage_management',
        'news_and_publication_management',
    ],
)
def get_api_v1__bills__bill_id__stages__stage_id__publications(
    bill_id: int = Path(..., alias='billId'), stage_id: int = Path(..., alias='stageId')
):
    """
    Return a list of Bill stage publications.
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get('/api/v1/PublicationTypes', tags=['news_and_publication_management'])
def get_api_v1__publication_types(
    skip: Optional[int] = Query(None, alias='Skip'),
    take: Optional[int] = Query(None, alias='Take'),
):
    """
    Returns a list of publication types.
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/api/v1/Publications/{publicationId}/Documents/{documentId}',
    tags=['news_and_publication_management'],
)
def get_api_v1__publications__publication_id__documents__document_id(
    publication_id: int = Path(..., alias='publicationId'),
    document_id: int = Path(..., alias='documentId'),
):
    """
    Return information on a document.
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/api/v1/Publications/{publicationId}/Documents/{documentId}/Download',
    tags=['news_and_publication_management'],
)
def retrieve_document_by_publication_id_and_document_id(
    publication_id: int = Path(..., alias='publicationId'),
    document_id: int = Path(..., alias='documentId'),
):
    """
    Return a document.
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get('/api/v1/Rss/Bills/{id}.rss', tags=['rss_feed_management', 'bill_management'])
def get_api_v1__rss__bills__id_rss(id: int):
    """
    Returns an Rss feed of a certain Bill.
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get('/api/v1/Rss/allbills.rss', tags=['bill_management', 'rss_feed_management'])
def get_api_v1__rss_allbills_rss():
    """
    Returns an Rss feed of all Bills.
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/api/v1/Rss/privatebills.rss', tags=['rss_feed_management', 'bill_management']
)
def get_api_v1__rss_privatebills_rss():
    """
    Returns an Rss feed of private Bills.
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get('/api/v1/Rss/publicbills.rss', tags=['rss_feed_management', 'bill_management'])
def get_api_v1__rss_publicbills_rss():
    """
    Returns an Rss feed of public Bills.
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get('/api/v1/Sittings', tags=['sittings_info_management'])
def get_sittings(
    house: Optional[House] = Query(None, alias='House'),
    date_from: Optional[datetime] = Query(None, alias='DateFrom'),
    date_to: Optional[datetime] = Query(None, alias='DateTo'),
    skip: Optional[int] = Query(None, alias='Skip'),
    take: Optional[int] = Query(None, alias='Take'),
):
    """
    Returns a list of Sittings.
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get('/api/v1/Stages', tags=['bill_stage_management', 'bill_management'])
def get_api_v1__stages(
    skip: Optional[int] = Query(None, alias='Skip'),
    take: Optional[int] = Query(None, alias='Take'),
):
    """
    Returns a list of Bill stages.
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
