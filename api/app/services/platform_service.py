from app.mock_data.data import ALERTS, DEPLOYMENTS, METRICS_SUMMARY, SERVICES


class PlatformService:
    def get_services(self) -> list[dict]:
        return SERVICES

    def get_service_by_id(self, service_id: str) -> dict | None:
        return next(
            (service for service in SERVICES if service["id"] == service_id),
            None,
        )

    def get_deployments(self) -> list[dict]:
        return DEPLOYMENTS

    def get_alerts(self) -> list[dict]:
        return ALERTS

    def get_metrics_summary(self) -> dict:
        return METRICS_SUMMARY


platform_service = PlatformService()