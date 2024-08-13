# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import pydantic_v1
from ..core.query_encoder import encode_query
from ..core.remove_none_from_dict import remove_none_from_dict
from ..core.request_options import RequestOptions
from ..types.get_scim_group_response import GetScimGroupResponse
from ..types.get_scim_user_response import GetScimUserResponse
from ..types.list_scim_groups_response import ListScimGroupsResponse
from ..types.list_scim_users_response import ListScimUsersResponse


class ScimClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_scim_groups(
        self,
        *,
        scim_directory_id: typing.Optional[str] = None,
        organization_id: typing.Optional[str] = None,
        organization_external_id: typing.Optional[str] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListScimGroupsResponse:
        """
        Parameters
        ----------
        scim_directory_id : typing.Optional[str]

        organization_id : typing.Optional[str]

        organization_external_id : typing.Optional[str]

        page_token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListScimGroupsResponse
            OK

        Examples
        --------
        from ssoready.client import SSOReady

        client = SSOReady(
            api_key="YOUR_API_KEY",
        )
        client.scim.list_scim_groups(
            organization_external_id="my_custom_external_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/scim/groups"),
            params=encode_query(
                jsonable_encoder(
                    remove_none_from_dict(
                        {
                            "scimDirectoryId": scim_directory_id,
                            "organizationId": organization_id,
                            "organizationExternalId": organization_external_id,
                            "pageToken": page_token,
                            **(
                                request_options.get("additional_query_parameters", {})
                                if request_options is not None
                                else {}
                            ),
                        }
                    )
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(ListScimGroupsResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_scim_group(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetScimGroupResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetScimGroupResponse
            OK

        Examples
        --------
        from ssoready.client import SSOReady

        client = SSOReady(
            api_key="YOUR_API_KEY",
        )
        client.scim.get_scim_group(
            id="scim_group_...",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v1/scim/groups/{jsonable_encoder(id)}"
            ),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(GetScimGroupResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list_scim_users(
        self,
        *,
        scim_directory_id: typing.Optional[str] = None,
        organization_id: typing.Optional[str] = None,
        organization_external_id: typing.Optional[str] = None,
        scim_group_id: typing.Optional[str] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListScimUsersResponse:
        """
        Parameters
        ----------
        scim_directory_id : typing.Optional[str]

        organization_id : typing.Optional[str]

        organization_external_id : typing.Optional[str]

        scim_group_id : typing.Optional[str]

        page_token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListScimUsersResponse
            OK

        Examples
        --------
        from ssoready.client import SSOReady

        client = SSOReady(
            api_key="YOUR_API_KEY",
        )
        client.scim.list_scim_users(
            organization_external_id="my_custom_external_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/scim/users"),
            params=encode_query(
                jsonable_encoder(
                    remove_none_from_dict(
                        {
                            "scimDirectoryId": scim_directory_id,
                            "organizationId": organization_id,
                            "organizationExternalId": organization_external_id,
                            "scimGroupId": scim_group_id,
                            "pageToken": page_token,
                            **(
                                request_options.get("additional_query_parameters", {})
                                if request_options is not None
                                else {}
                            ),
                        }
                    )
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(ListScimUsersResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_scim_user(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetScimUserResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetScimUserResponse
            OK

        Examples
        --------
        from ssoready.client import SSOReady

        client = SSOReady(
            api_key="YOUR_API_KEY",
        )
        client.scim.get_scim_user(
            id="scim_user_...",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v1/scim/users/{jsonable_encoder(id)}"
            ),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(GetScimUserResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncScimClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_scim_groups(
        self,
        *,
        scim_directory_id: typing.Optional[str] = None,
        organization_id: typing.Optional[str] = None,
        organization_external_id: typing.Optional[str] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListScimGroupsResponse:
        """
        Parameters
        ----------
        scim_directory_id : typing.Optional[str]

        organization_id : typing.Optional[str]

        organization_external_id : typing.Optional[str]

        page_token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListScimGroupsResponse
            OK

        Examples
        --------
        from ssoready.client import AsyncSSOReady

        client = AsyncSSOReady(
            api_key="YOUR_API_KEY",
        )
        await client.scim.list_scim_groups(
            organization_external_id="my_custom_external_id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/scim/groups"),
            params=encode_query(
                jsonable_encoder(
                    remove_none_from_dict(
                        {
                            "scimDirectoryId": scim_directory_id,
                            "organizationId": organization_id,
                            "organizationExternalId": organization_external_id,
                            "pageToken": page_token,
                            **(
                                request_options.get("additional_query_parameters", {})
                                if request_options is not None
                                else {}
                            ),
                        }
                    )
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(ListScimGroupsResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_scim_group(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetScimGroupResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetScimGroupResponse
            OK

        Examples
        --------
        from ssoready.client import AsyncSSOReady

        client = AsyncSSOReady(
            api_key="YOUR_API_KEY",
        )
        await client.scim.get_scim_group(
            id="scim_group_...",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v1/scim/groups/{jsonable_encoder(id)}"
            ),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(GetScimGroupResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list_scim_users(
        self,
        *,
        scim_directory_id: typing.Optional[str] = None,
        organization_id: typing.Optional[str] = None,
        organization_external_id: typing.Optional[str] = None,
        scim_group_id: typing.Optional[str] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListScimUsersResponse:
        """
        Parameters
        ----------
        scim_directory_id : typing.Optional[str]

        organization_id : typing.Optional[str]

        organization_external_id : typing.Optional[str]

        scim_group_id : typing.Optional[str]

        page_token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListScimUsersResponse
            OK

        Examples
        --------
        from ssoready.client import AsyncSSOReady

        client = AsyncSSOReady(
            api_key="YOUR_API_KEY",
        )
        await client.scim.list_scim_users(
            organization_external_id="my_custom_external_id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/scim/users"),
            params=encode_query(
                jsonable_encoder(
                    remove_none_from_dict(
                        {
                            "scimDirectoryId": scim_directory_id,
                            "organizationId": organization_id,
                            "organizationExternalId": organization_external_id,
                            "scimGroupId": scim_group_id,
                            "pageToken": page_token,
                            **(
                                request_options.get("additional_query_parameters", {})
                                if request_options is not None
                                else {}
                            ),
                        }
                    )
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(ListScimUsersResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_scim_user(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetScimUserResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetScimUserResponse
            OK

        Examples
        --------
        from ssoready.client import AsyncSSOReady

        client = AsyncSSOReady(
            api_key="YOUR_API_KEY",
        )
        await client.scim.get_scim_user(
            id="scim_user_...",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v1/scim/users/{jsonable_encoder(id)}"
            ),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(GetScimUserResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
